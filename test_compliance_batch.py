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
    
    def test_valid_sitdocto(self):
        """Test that valid_sitdocto is set to '00'."""
        self.assertEqual(self.batch_builder.valid_sitdocto, '00')
    
    def test_query_returns_tuple(self):
        """Test that build_query returns a tuple of (query, parameters)."""
        result = self.batch_builder.build_query()
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
    
    def test_query_contains_sitdocto_filter(self):
        """Test that query includes sitdocto parameterized filter to exclude cancelled invoices."""
        query, params = self.batch_builder.build_query()
        self.assertIn("sitdocto = ?", query)
        self.assertIn('00', params)
    
    def test_query_contains_tipoobjintegr_filter(self):
        """Test that query includes tipoobjintegr_id parameterized filter."""
        query, params = self.batch_builder.build_query()
        self.assertIn("tipoobjintegr_id = ?", query)
        self.assertIn(24, params)
    
    def test_query_uses_nota_fiscal_servico_table(self):
        """Test that query selects from nota_fiscal_servico table."""
        query, params = self.batch_builder.build_query()
        self.assertIn("nota_fiscal_servico", query)
    
    def test_query_has_both_filters(self):
        """Test that query has both required filters combined with AND."""
        query, params = self.batch_builder.build_query()
        self.assertIn("tipoobjintegr_id = ?", query)
        self.assertIn("AND", query)
        self.assertIn("sitdocto = ?", query)
        self.assertEqual(params, (24, '00'))
    
    def test_parameters_correct_order(self):
        """Test that parameters are in correct order."""
        query, params = self.batch_builder.build_query()
        self.assertEqual(params, (24, '00'))


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
    
    def test_valid_sitdocto(self):
        """Test that valid_sitdocto is set to '00'."""
        self.assertEqual(self.batch_builder.valid_sitdocto, '00')
    
    def test_query_returns_tuple(self):
        """Test that build_query returns a tuple of (query, parameters)."""
        result = self.batch_builder.build_query()
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
    
    def test_query_contains_sitdocto_filter(self):
        """Test that query includes sitdocto parameterized filter to exclude cancelled invoices."""
        query, params = self.batch_builder.build_query()
        self.assertIn("sitdocto = ?", query)
        self.assertIn('00', params)
    
    def test_query_contains_tipoobjintegr_filter(self):
        """Test that query includes tipoobjintegr_id parameterized filter."""
        query, params = self.batch_builder.build_query()
        self.assertIn("tipoobjintegr_id = ?", query)
        self.assertIn(24, params)
    
    def test_query_uses_nota_fiscal_servico_table(self):
        """Test that query selects from nota_fiscal_servico table."""
        query, params = self.batch_builder.build_query()
        self.assertIn("nota_fiscal_servico", query)
    
    def test_query_has_both_filters(self):
        """Test that query has both required filters combined with AND."""
        query, params = self.batch_builder.build_query()
        self.assertIn("tipoobjintegr_id = ?", query)
        self.assertIn("AND", query)
        self.assertIn("sitdocto = ?", query)
        self.assertEqual(params, (24, '00'))
    
    def test_parameters_correct_order(self):
        """Test that parameters are in correct order."""
        query, params = self.batch_builder.build_query()
        self.assertEqual(params, (24, '00'))


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
