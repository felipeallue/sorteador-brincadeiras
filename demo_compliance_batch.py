"""
Demonstration script for compliance batch SQL query generation.
Shows how the queries properly filter cancelled invoices for both BRHUB and SuiteApps.
"""

from compliance_batch import get_compliance_batch_builder


def main():
    """Demonstrate the SQL query generation for both integration models."""
    
    print("=" * 80)
    print("COMPLIANCE BATCH - SQL QUERY DEMONSTRATION")
    print("Third-Party Service Invoices (tipoobjintegr_id = 24)")
    print("=" * 80)
    print()
    
    # BRHUB Integration Model
    print("1. BRHUB Integration Model")
    print("-" * 80)
    brhub_builder = get_compliance_batch_builder('BRHUB')
    brhub_query = brhub_builder.build_query()
    print(brhub_query)
    print()
    print("Key Features:")
    print("  ✓ Filters by tipoobjintegr_id = 24 (third-party service invoices)")
    print("  ✓ Filters by sitdocto = '00' (excludes cancelled invoices)")
    print("  ✓ Selects from nota_fiscal_servico table")
    print()
    print()
    
    # SuiteApps Integration Model
    print("2. SuiteApps Integration Model")
    print("-" * 80)
    suiteapps_builder = get_compliance_batch_builder('SuiteApps')
    suiteapps_query = suiteapps_builder.build_query()
    print(suiteapps_query)
    print()
    print("Key Features:")
    print("  ✓ Filters by tipoobjintegr_id = 24 (third-party service invoices)")
    print("  ✓ Filters by sitdocto = '00' (excludes cancelled invoices)")
    print("  ✓ Selects from nota_fiscal_servico table")
    print()
    print()
    
    # Summary
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print()
    print("Both integration models (BRHUB and SuiteApps) now include the restriction:")
    print("  AND sitdocto = '00'")
    print()
    print("This ensures that cancelled invoices are NOT included in the compliance batch.")
    print("Only valid invoices (sitdocto = '00') will be sent for integration.")
    print()


if __name__ == '__main__':
    main()
