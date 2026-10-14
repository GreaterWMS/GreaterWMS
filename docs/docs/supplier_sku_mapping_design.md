# Supplier-SKU Mapping Design

## Objective
Define a structured relationship between suppliers and SKUs to support procurement and inventory planning.

## Problem
Each SKU can have multiple suppliers with different lead times, costs, and reliability. Without structured mapping, procurement decisions are inefficient and error-prone.

## Proposed Solution

Introduce a Supplier-SKU mapping model that includes:

- Supplier ID
- SKU ID
- Lead time (days)
- Minimum order quantity (MOQ)
- Cost or pricing reference
- Preferred supplier flag

## Key Workflows

### Supplier Assignment
Assign one or more suppliers to each SKU.

### Supplier Selection
Select supplier based on:
- Lead time
- Cost
- Performance

### Replenishment Integration
Use Supplier-SKU data in inventory replenishment logic.

## Impact

- Improved procurement decisions
- Better supplier selection
- More accurate inventory planning

## Next Steps

- Define database schema
- Create API endpoints
- Integrate with procurement workflows
