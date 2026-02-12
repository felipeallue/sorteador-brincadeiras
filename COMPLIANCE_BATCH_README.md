# Compliance Batch - Cancelled Invoice Filter

## Overview

This implementation adds a restriction to the compliance batch assembly for third-party service invoices to exclude cancelled invoices from being sent to integration systems.

## Issue Resolution

**Issue #11**: Na montagem de lote compliance de nota de serviço de terceiros (tipoobjintegr_id = 24), colocar restrição no select para que notas canceladas não sejam enviadas.

### Solution

Added the SQL clause `AND sitdocto = '00'` to the SELECT queries that fetch invoices from the `nota_fiscal_servico` table. This applies to both integration models:
- BRHUB
- SuiteApps

## Implementation Details

### Files Created

1. **compliance_batch.py** - Core module containing:
   - `ComplianceBatchBuilder`: Base class for compliance batch builders
   - `BRHUBComplianceBatch`: BRHUB integration implementation
   - `SuiteAppsComplianceBatch`: SuiteApps integration implementation
   - `get_compliance_batch_builder()`: Factory function to get the appropriate builder

2. **test_compliance_batch.py** - Comprehensive test suite:
   - 15 unit tests validating the implementation
   - Tests for both BRHUB and SuiteApps models
   - Validates presence of required filters
   - All tests passing ✓

3. **demo_compliance_batch.py** - Demonstration script:
   - Shows the generated SQL queries
   - Highlights the key features
   - Displays the sitdocto filter in action

## SQL Query Structure

Both integration models now generate queries with the following structure:

```sql
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
    nfs.tipoobjintegr_id = 24
    AND nfs.sitdocto = '00'
ORDER BY 
    nfs.data_emissao DESC
```

### Key Filters

1. **tipoobjintegr_id = 24**: Selects only third-party service invoices
2. **sitdocto = '00'**: Excludes cancelled invoices (only includes valid invoices)

## Usage

```python
from compliance_batch import get_compliance_batch_builder

# Get BRHUB builder
brhub_builder = get_compliance_batch_builder('BRHUB')
brhub_query = brhub_builder.build_query()

# Get SuiteApps builder
suiteapps_builder = get_compliance_batch_builder('SuiteApps')
suiteapps_query = suiteapps_builder.build_query()
```

## Testing

Run the test suite:
```bash
python -m unittest test_compliance_batch.py -v
```

Run the demonstration:
```bash
python demo_compliance_batch.py
```

## Impact

- **Before**: Cancelled invoices (sitdocto != '00') were included in compliance batches
- **After**: Only valid invoices (sitdocto = '00') are included in compliance batches
- **Integration Models Affected**: BRHUB and SuiteApps

## Validation

All 15 unit tests pass, confirming:
- ✓ Correct integration model identification
- ✓ Correct tipoobjintegr_id value (24)
- ✓ Presence of sitdocto = '00' filter
- ✓ Presence of tipoobjintegr_id = 24 filter
- ✓ Correct table name (nota_fiscal_servico)
- ✓ Proper AND clause combining both filters
- ✓ Factory function returns correct builder types
