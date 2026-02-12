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
   - `ComplianceBatchBuilder`: Base class for compliance batch builders with shared query logic
   - `BRHUBComplianceBatch`: BRHUB integration implementation
   - `SuiteAppsComplianceBatch`: SuiteApps integration implementation
   - `get_compliance_batch_builder()`: Factory function to get the appropriate builder
   - **Security**: Uses parameterized queries to prevent SQL injection

2. **test_compliance_batch.py** - Comprehensive test suite:
   - 21 unit tests validating the implementation
   - Tests for both BRHUB and SuiteApps models
   - Validates presence of required filters
   - Tests parameterized query structure
   - All tests passing ✓

3. **demo_compliance_batch.py** - Demonstration script:
   - Shows the generated SQL queries
   - Highlights the key features
   - Displays the sitdocto filter in action
   - Shows secure parameterized query usage

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
    nfs.tipoobjintegr_id = ?
    AND nfs.sitdocto = ?
ORDER BY 
    nfs.data_emissao DESC
```

**Parameters**: `(24, '00')`

### Key Filters

1. **tipoobjintegr_id = ?**: Selects only third-party service invoices (parameter: 24)
2. **sitdocto = ?**: Excludes cancelled invoices (parameter: '00' = valid invoices only)

### Security Features

- **Parameterized queries**: All SQL queries use placeholders (?) instead of direct value interpolation
- **SQL injection prevention**: Parameters are passed separately from the query string
- **No code duplication**: Common query logic is in the base class

## Usage

```python
from compliance_batch import get_compliance_batch_builder

# Get BRHUB builder
brhub_builder = get_compliance_batch_builder('BRHUB')
query, params = brhub_builder.build_query()
# Execute with: cursor.execute(query, params)

# Get SuiteApps builder
suiteapps_builder = get_compliance_batch_builder('SuiteApps')
query, params = suiteapps_builder.build_query()
# Execute with: cursor.execute(query, params)
```

**Important**: Always use the parameterized query format:
```python
cursor.execute(query, params)  # Secure
# NOT: cursor.execute(query % params)  # Insecure!
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

All 21 unit tests pass, confirming:
- ✓ Correct integration model identification
- ✓ Correct tipoobjintegr_id value (24)
- ✓ Correct valid_sitdocto value ('00')
- ✓ Query returns tuple (query, parameters)
- ✓ Presence of parameterized sitdocto filter
- ✓ Presence of parameterized tipoobjintegr_id filter
- ✓ Correct table name (nota_fiscal_servico)
- ✓ Proper AND clause combining both filters
- ✓ Correct parameter order in tuple
- ✓ Factory function returns correct builder types
- ✓ No SQL injection vulnerabilities (parameterized queries)
