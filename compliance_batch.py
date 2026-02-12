"""
Compliance Batch Module for Third-Party Service Invoices
Handles batch assembly for integration with BRHUB and SuiteApps systems.
"""


class ComplianceBatchBuilder:
    """Base class for building compliance batches for fiscal invoice integration."""
    
    def __init__(self, integration_model):
        """
        Initialize the compliance batch builder.
        
        Args:
            integration_model: The integration model type ('BRHUB' or 'SuiteApps')
        """
        self.integration_model = integration_model
        self.tipoobjintegr_id = 24  # Third-party service invoices
        self.valid_sitdocto = '00'  # Valid document status (non-cancelled)
    
    def build_query(self):
        """
        Build SQL query to fetch service invoices from nota_fiscal_servico table.
        
        This query includes:
        - Filter for tipoobjintegr_id = 24 (third-party service invoices)
        - Filter for sitdocto = '00' (exclude cancelled invoices)
        
        Returns:
            tuple: (query_string, parameters) for use with parameterized queries
        """
        query = """
        SELECT 
            nfs.id,
            nfs.numero_nota,
            nfs.data_emissao,
            nfs.valor_total,
            nfs.prestador_id,
            nfs.tomador_id,
            nfs.sitdocto,
            nfs.tipoobjintegr_id
        FROM 
            nota_fiscal_servico nfs
        WHERE 
            nfs.tipoobjintegr_id = ?
            AND nfs.sitdocto = ?
        ORDER BY 
            nfs.data_emissao DESC
        """
        parameters = (self.tipoobjintegr_id, self.valid_sitdocto)
        return query.strip(), parameters


class BRHUBComplianceBatch(ComplianceBatchBuilder):
    """Compliance batch builder for BRHUB integration model."""
    
    def __init__(self):
        super().__init__('BRHUB')


class SuiteAppsComplianceBatch(ComplianceBatchBuilder):
    """Compliance batch builder for SuiteApps integration model."""
    
    def __init__(self):
        super().__init__('SuiteApps')


def get_compliance_batch_builder(integration_model):
    """
    Factory function to get the appropriate compliance batch builder.
    
    Args:
        integration_model: The integration model type ('BRHUB' or 'SuiteApps')
    
    Returns:
        ComplianceBatchBuilder: Instance of the appropriate batch builder
    
    Raises:
        ValueError: If integration_model is not supported
    """
    if integration_model == 'BRHUB':
        return BRHUBComplianceBatch()
    elif integration_model == 'SuiteApps':
        return SuiteAppsComplianceBatch()
    else:
        raise ValueError(f"Unsupported integration model: {integration_model}")
