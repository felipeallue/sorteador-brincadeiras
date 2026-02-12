"""
Tests for compliance batch module.
Validates that SQL queries properly filter cancelled invoices.
"""

import unittest
from compliance_batch import (
    BRHUBComplianceBatch,
    SuiteAppsComplianceBatch,
    get_compliance_batch_builder
)


class TestBRHUBComplianceBatch(unittest.TestCase):
    """Test cases for BRHUB integration model."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.batch_builder = BRHUBComplianceBatch()
    
    def test_integration_model(self):
        """Test that integration model is correctly set."""
        self.assertEqual(self.batch_builder.integration_model, 'BRHUB')
    
    def test_tipoobjintegr_id(self):
        """Test that tipoobjintegr_id is set to 24."""
        self.assertEqual(self.batch_builder.tipoobjintegr_id, 24)
    
    def test_query_contains_sitdocto_filter(self):
        """Test that query includes sitdocto = '00' filter to exclude cancelled invoices."""
        query = self.batch_builder.build_query()
        self.assertIn("sitdocto = '00'", query)
    
    def test_query_contains_tipoobjintegr_filter(self):
        """Test that query includes tipoobjintegr_id = 24 filter."""
        query = self.batch_builder.build_query()
        self.assertIn("tipoobjintegr_id = 24", query)
    
    def test_query_uses_nota_fiscal_servico_table(self):
        """Test that query selects from nota_fiscal_servico table."""
        query = self.batch_builder.build_query()
        self.assertIn("nota_fiscal_servico", query)
    
    def test_query_has_both_filters(self):
        """Test that query has both required filters combined with AND."""
        query = self.batch_builder.build_query()
        self.assertIn("tipoobjintegr_id = 24", query)
        self.assertIn("AND", query)
        self.assertIn("sitdocto = '00'", query)


class TestSuiteAppsComplianceBatch(unittest.TestCase):
    """Test cases for SuiteApps integration model."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.batch_builder = SuiteAppsComplianceBatch()
    
    def test_integration_model(self):
        """Test that integration model is correctly set."""
        self.assertEqual(self.batch_builder.integration_model, 'SuiteApps')
    
    def test_tipoobjintegr_id(self):
        """Test that tipoobjintegr_id is set to 24."""
        self.assertEqual(self.batch_builder.tipoobjintegr_id, 24)
    
    def test_query_contains_sitdocto_filter(self):
        """Test that query includes sitdocto = '00' filter to exclude cancelled invoices."""
        query = self.batch_builder.build_query()
        self.assertIn("sitdocto = '00'", query)
    
    def test_query_contains_tipoobjintegr_filter(self):
        """Test that query includes tipoobjintegr_id = 24 filter."""
        query = self.batch_builder.build_query()
        self.assertIn("tipoobjintegr_id = 24", query)
    
    def test_query_uses_nota_fiscal_servico_table(self):
        """Test that query selects from nota_fiscal_servico table."""
        query = self.batch_builder.build_query()
        self.assertIn("nota_fiscal_servico", query)
    
    def test_query_has_both_filters(self):
        """Test that query has both required filters combined with AND."""
        query = self.batch_builder.build_query()
        self.assertIn("tipoobjintegr_id = 24", query)
        self.assertIn("AND", query)
        self.assertIn("sitdocto = '00'", query)


class TestComplianceBatchFactory(unittest.TestCase):
    """Test cases for the factory function."""
    
    def test_get_brhub_builder(self):
        """Test that factory returns BRHUB builder."""
        builder = get_compliance_batch_builder('BRHUB')
        self.assertIsInstance(builder, BRHUBComplianceBatch)
    
    def test_get_suiteapps_builder(self):
        """Test that factory returns SuiteApps builder."""
        builder = get_compliance_batch_builder('SuiteApps')
        self.assertIsInstance(builder, SuiteAppsComplianceBatch)
    
    def test_invalid_integration_model(self):
        """Test that factory raises ValueError for invalid model."""
        with self.assertRaises(ValueError):
            get_compliance_batch_builder('InvalidModel')


if __name__ == '__main__':
    unittest.main()
