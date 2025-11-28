Product (Version 2)
===================

Product

Service name: Product

This synchronous inbound service enables you to create, read, update, and delete (CRUD operations) the master data for products by exposing the remote API views through OData V4.

This service is published on the SAP Business Accelerator Hub. For more information about APIs, see [APIs on SAP Business Accelerator Hub](https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/1e60f14bdc224c2c975c8fa8bcfd7f3f.html?locale=en-US&state=PRODUCTION&version=2508.500).

This is an OData version 4 service. This version aims to improve processing time and resource consumption of clients and servers. This includes a lightweight JSON format that reduces the size of every response.

Technical Details
-----------------

A service group contains services belonging to the same business object model and so it shares similar environment conditions. This means the configuration and administration of a service group apply to all services in a service group, that is, routing, authorization, and so on, so you only have to do them once.

In the OData version 4 (V4) runtime implementation of the SAP Gateway Foundation, framework services originate from repositories.

Service Group (incl. Namespace if Existent)

Repository ID

Service Name (incl. Namespace if Existent)

Version

API\_PRODUCT

srvd\_a2x

PRODUCT

0002

Extensibility
-------------

You can extend the following entities for product master data using the app Custom Fields and Logic (available on SAP Fiori Launchpad) to add custom fields as per requirements:

*   A\_ProdPlantQualityManagement\_3
    
*   A\_ProdPlantStorageLocation\_3
    
*   A\_ProdPlantInternationalTrade\_3
    
*   A\_Product\_3
    
*   A\_ProductPlant\_3
    
*   A\_ProductPlantCosting\_3
    
*   A\_ProductPlantForecast\_3
    
*   A\_ProductPlantProcurement\_3
    
*   A\_ProductPlantSales\_3
    
*   A\_ProductPlantStorage\_3
    
*   A\_ProductPlantSupplyPlanning\_3
    
*   A\_ProductPlantWorkScheduling\_3
    
*   A\_ProductProcurement\_3
    
*   A\_ProductQualityManagement\_3
    
*   A\_ProductSales\_3
    
*   A\_ProductSalesDelivery\_3
    
*   A\_ProductStorage\_3
    
*   A\_ProductUnitOfMeasure\_3
    
*   A\_ProductValuation\_3
    
*   A\_ProductValuationAccounting\_3
    
*   A\_ProductValuationCosting\_3
    
*   A\_ProdValuationLedgerAccount\_3
    
*   A\_ProductEWMWarehouse\_3
    
*   A\_ProductEWMStorageType\_3
    

Service Structure
-----------------

Service Header (optional)

The service header contains information about the service.

Entities

The entities contain the business data of the service.

Product

(Product)

Product

Optional

[Product](https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/45432b0348ee48b1b649b8a322d503d4.html?locale=en-US&state=PRODUCTION&version=2508.500)

Product Description (ProductDescription)

Description of product

Optional

[Product Description](https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/ec28ca41bd32431392ab10d45e9ea6b7.html?locale=en-US&state=PRODUCTION&version=2508.500)

Product EWM Storage Type(ProductEWMStorageType)

EWM storage type related data of product

Optional

[Product EWM Storage Type](https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/83bff663160d4df89a03e1307832de8d.html?locale=en-US&state=PRODUCTION&version=2508.500)

Product EWM Warehouse(ProductEWMWarehouse)

EWM warehouse related data of product

Optional

[Product EWM Warehouse](https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/7eec77ebd3c74be19601f7d7289219f3.html?locale=en-US&state=PRODUCTION&version=2508.500)

Product Plant (ProductPlant)

Plant related data of product

Optional

[Product Plant](https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/b15efbbf7bda4342beebe25f818e59e8.html?locale=en-US&state=PRODUCTION&version=2508.500)

Product Plant Costing (ProductPlantCosting)

Costing related data for plant

Optional

[Product Plant Costing](https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/13ece53f23d446d9a56c2f7756e451cb.html?locale=en-US&state=PRODUCTION&version=2508.500)

Product Plant Forecast (ProductPlantForecast)

Plant related forecast information of product

Optional

[Product Plant Forecast](https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/d6573a6063a84b90b0f37fb41f99781e.html?locale=en-US&state=PRODUCTION&version=2508.500)

Product Plant Inspection Type Setting (ProductPlantspTypeSetting)

Inspection type setting information of product plant

Optional

[Product Plant Inspection Type Setting](https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/4563025c6db74cc48eda0425b00087b4.html?locale=en-US&state=PRODUCTION&version=2508.500)

Product Plant International Trade (ProdPlantInternationalTrade)

International trade information of product plant

Optional

[Product Plant International Trade](https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/e301ad93287942f59a27462bcdef98f9.html?locale=en-US&state=PRODUCTION&version=2508.500)

Product Plant MRP (ProductPlantMRP)

Maximum retail price (MRP) of product plant

Optional

[Product Plant MRP](https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/97560137bc4640b9950c576d3c0870a3.html?locale=en-US&state=PRODUCTION&version=2508.500)

Product Plant Sales (ProductPlantSales)

Sales information of product plant

Optional

[Product Plant Sales](https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/b5fd818c040447aeba21bc9e70c345cb.html?locale=en-US&state=PRODUCTION&version=2508.500)

Product Plant Storage (ProductPlantStorage)

Plant related storage details of product

Optional

[Product Plant Storage](https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/d8a3818df4664d4c9909ed44a414fba3.html?locale=en-US&state=PRODUCTION&version=2508.500)

Product Plant Storage Location (ProductPlantStorageLocation)

Plant related storage location details of product

Optional

[Product Plant Storage Location](https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/27cac5f983d942929a5be4d0388a23ad.html?locale=en-US&state=PRODUCTION&version=2508.500)

Product Plant Supply Planning (ProductPlantSupplyPlanning)

Supply planning related data for plant

Optional

[Product Plant Supply Planning](https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/82080bbcc54b4291bdb6b6e4e0c6056e.html?locale=en-US&state=PRODUCTION&version=2508.500)

Product Plant Work Scheduling (ProductPlantWorkScheduling)

Work scheduling related data for plant

Optional

[Product Plant Work Scheduling](https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/617cf94f921c40ffb6b86407cf059381.html?locale=en-US&state=PRODUCTION&version=2508.500)

Product Procurement (ProductProcurement)

Procurement related data of product

Optional

[Product Procurement](https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/e449d4f0aa3a48b289777f22828b0bb3.html?locale=en-US&state=PRODUCTION&version=2508.500)

Product Quality Management (ProductQualityManagement)

Quality management related data of product

Optional

[Product Quality Management](https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/718d99c89887440da28fe214c992d7b5.html?locale=en-US&state=PRODUCTION&version=2508.500)

Product Sales (ProductSales)

Sales related data of product

Optional

[Product Sales](https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/7de6e5af1e9d498f99c68073f598626c.html?locale=en-US&state=PRODUCTION&version=2508.500)

Product Sales Delivery (ProductSalesDelivery)

Sales delivery related data of product

Optional

[Product Sales Delivery](https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/7fc6f54f569e43b2a6b04ea6640f3735.html?locale=en-US&state=PRODUCTION&version=2508.500)

Product Sales Delivery Sales Tax (ProductSalesDeliverySalesTax)

Sales tax related data for product's sales delivery

Optional

[Product Sales Delivery Sales Tax](https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/3c863dbaf8644a44b50956d744142616.html?locale=en-US&state=PRODUCTION&version=2508.500)

Product Unit of Measure (ProductUnitofMeasure)

Units of measure related data of product

Optional

[Product Units Of Measure](https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/4985a85d4468478896508e71beecbfe4.html?locale=en-US&state=PRODUCTION&version=2508.500)

Product Unit of Measure EAN (ProductUnitofMeasureEAN)

EAN data of a product's units of measure

Optional

[Product Units of Measure EAN](https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/29f86f9a8de04085910e9393367d9064.html?locale=en-US&state=PRODUCTION&version=2508.500)

Product Valuation (ProductValuation)

Valuation related data of product

[Product Valuation](https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/772bf4b02b4245d9912a2b04cd042643.html?locale=en-US&state=PRODUCTION&version=2508.500)

Product Valuation Accounting (ProductValuationAccounting)

Valuation accounting related data of product

Optional

[Product Valuation Accounting](https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/258aa688596a4131a9bfedaf694edd75.html?locale=en-US&state=PRODUCTION&version=2508.500)

Product Valuation Costing (ProductValuationCosting)

Valuation costing related data of product

Optional

[Product Valuation Costing](https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/dc7ce837413f41f285c17c4df3697f9d.html?locale=en-US&state=PRODUCTION&version=2508.500)

Product Valuation Ledger Account (ProductValuationLedge Account)

Valuation ledger account related data of product

Optional

[Product Valuation Ledger Account](https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/0257f5c338f3410da7570aab16cb673e.html?locale=en-US&state=PRODUCTION&version=2508.500)

Product Valuation Ledger Prices (ProductValuationLedgerPrices)

Valuation ledger prices related data of product

Optional

[Product Valuation Ledger Prices](https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/36eeeab42c0f41a99edda29c040e3f55.html?locale=en-US&state=PRODUCTION&version=2508.500)

Page size:

Showing 1–27 of 27

Service Response
----------------

Page size:**10**

Showing 1 of 1

### Error Codes

200

OK

201

Created

202

Accepted

204

No Content

400

Bad Request

403

Forbidden

404

Resource Not Found

500

Internal Server Error

Page size:**10**

Showing 1–8 of 8

Constraints
-----------

This service interface is released with the following restrictions. For more information, contact your SAP system administrator.

*   You can't change the product type. To change the material type, use the Change Material Type app. For more information, see [Changing a Material Type](https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/115fb5ab17314c8da5233739873d22c4.html?locale=en-US&state=PRODUCTION&version=2508.500 "In certain circumstances, it may be necessary to change the material type. For example, a material that was always procured externally in the past and whose material type allows only external procurement is also to be produced in-house in the future. Therefore, you must assign the material to a material type that also allows in-house production.").
    
*   When you try to delete master data records using this OData service, note that only the entities that are listed above, get deleted. For the other entries, you should set a a flag at the required entity level, such that the data will be marked for archiving. You can set this deletion indicator using the PATCH or PUT operation while updating the product master data record.
    
*   This service does not support the maintenance of retail articles. SAP recommends that you do not use this service to read the data for the same as well.
    
*   This service does not support RITA . For more information, refer to [Registration for Indirect Taxation Abroad (RITA) in Product Master Data](https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/3679262219a14fed9f715143ead46a86.html?locale=en-US&state=PRODUCTION&version=2508.500)
    
*   This service currently supports only external number ranges.
    

Authentication
--------------

The API is based on the OData V4 protocol.

Related Events
--------------

*   [Product Events](https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/a05a6c9d839e45aaa48790c1a4099fab.html?locale=en-US&state=PRODUCTION&version=2508.500 "Business Event Handling for Products")
    

Additional Information
----------------------

 **Note**

For more details about Communication Management, see [Communication Management](https://help.sap.com/docs/SAP_S4HANA_CLOUD/3c916ef10fc240c9afc594b346ffaf77/2e84a10c430645a88bdbfaaa23ac9ff7.html?locale=en-US&state=PRODUCTION&version=2508.500 "The communication management apps allow you to integrate your system or solution with other systems to enable data exchange.").

Operations for Product API
==========================

The Product (API\_PRODUCT) API offers these operations:

Create product master data

POST

POST <host>/sap/opu/odata4/sap/api\_product/srvd\_a2x/sap/product/0002/Product

Delete product master data

DELETE

POST <host>/sap/opu/odata4/sap/api\_product/srvd\_a2x/sap/product/0002/ProductDescription(Product='TG-17',Language='BG')

Read product master data

GET

GET <host> /sap/opu/odata4/sap/api\_product/srvd\_a2x/sap/product/0002/Product('TG-17')

Update product master data

PATCH, PUT

PATCH <host>/sap/opu/odata4/sap/api\_product/srvd\_a2x/sap/product/0002/Product

Page size:**10**

Showing 1–4 of 4

Change Sets
-----------

ETags
-----

The API uses entity tags (ETags) for optimistic concurrency control. That is, if a client requests a modification of a resource on the back-end server, the ETags of the resource on the client server and on the back-end server are compared to determine whether any changes were made to the resource on the back-end server. For this API, the If-Match header must be set for all change operations.

Read Product Master Data Record
===============================

Request
-------

You can include the following properties in the request's URL:

ProdSalesDeliverySalesTax

Optional

Product

Mandatory

ProductChangeMaster

Optional

ProductDescription

Optional

ProductEWMStorageType

Optional

ProductEWMWarehouse

Optional

ProductPlant

Optional

ProductPlantCosting

Optional

ProductPlantPlanning

Optional

ProductPlantspectionTypeSetting

Optional

ProductPlantSupplyPlanning

Optional

ProductPlantSupplyPlanning

Optional

ProductPlantWorkScheduling

Optional

ProductProcurement

Optional

ProductQualityManagement

Optional

ProductSales

Optional

ProductSalesDelivery

Optional

ProductUnitOfMeasure

Optional

ProductUnitOfMeasureEAN

Optional

ProductValuation

Optional

ProductValuationAccounting

Optional

ProductValuationCosting

Optional

ProductValuationLedge Account

Optional

ProductValuationLedgerPrices

Optional

Page size:

Showing 1–24 of 24

Response
--------

This operation returns all the product master data records.

Examples
--------

### Request

 **Sample Code**

    GET <host>/sap/opu/odata4/sap/api_product/srvd_a2x/sap/product/0002/Product('TE140721_2')
    
    

### Response

### Success Response

 **Sample Code**

    {
        "@odata.context": "$metadata#Product/$entity",
        "@odata.metadataEtag": "W/\"20210915002329\"",
        "@odata.etag": "W/\"SADL-202107211113230000000C~20210721111323.0000000\"",
        "Product": "TE140721_2",
        "ProductType": "FERT",
        "CreationDate": "2021-07-14",
        "CreationTime": "11:24:59",
        "CreationDateTime": "2021-07-14T11:24:59Z",
        "CreatedByUser": "_SAP19148",
        "LastChangeDate": "2021-07-21",
        "LastChangedByUser": "_SAP19148",
        "IsMarkedForDeletion": true,
       "CrossPlantStatus": "02",
        "CrossPlantStatusValidityDate": "2021-07-15",
        "ProductOldID": "100",
        "GrossWeight": 10.000,
        "WeightUnit": "KG",
        "WeightISOUnit": "KGM",
        "ProductGroup": "A002",
        "BaseUnit": "MM",
        "BaseISOUnit": "MMT",
        "ItemCategoryGroup": "0002",
        "NetWeight": 10.000,
        "Division": "00",
        "VolumeUnit": "CCM",
        "VolumeISOUnit": "CMQ",
        "ProductVolume": 10.000,
        "AuthorizationGroup": "100",
        "ANPCode": "110101004",
        "SizeOrDimensionText": "TEXT",
        "IndustryStandardName": "INDUSTRY",
        "ProductStandardID": "2150000000000",
        "InternationalArticleNumberCat": "EA",
        "ProductIsConfigurable": true,
        "IsBatchManagementRequired": true,
        "ExternalProductGroup": "",
        "CrossPlantConfigurableProduct": "",
        "SerialNoExplicitnessLevel": "1",
        "IsApprovedBatchRecordReqd": true,
        "HandlingIndicator": "",
        "WarehouseProductGroup": "",
        "WarehouseStorageCondition": "",
        "StandardHandlingUnitType": "SP1",
        "SerialNumberProfile": "",
        "IsPilferable": true,
        "IsRelevantForHzdsSubstances": true,
        "QuarantinePeriod": 10,
        "TimeUnitForQuarantinePeriod": "WMP",
        "QuarantinePeriodISOUnit": "",
        "QualityInspectionGroup": "",
        "HandlingUnitType": "SP1",
        "HasVariableTareWeight": true,
        "MaximumPackagingLength": 10.000,
        "MaximumPackagingWidth": 10.000,
        "MaximumPackagingHeight": 10.000,
        "MaximumCapacity": 10.000,
        "OvercapacityTolerance": 10.0,
        "UnitForMaxPackagingDimensions": "CM",
        "MaxPackggDimensionISOUnit": "CMT",
        "BaseUnitSpecificProductLength": 10.000,
        "BaseUnitSpecificProductWidth": 10.000,
        "BaseUnitSpecificProductHeight": 10.000,
        "ProductMeasurementUnit": "CM",
        "ProductMeasurementISOUnit": "CMT",
        "ArticleCategory": "",
        "IndustrySector": "M",
        "LastChangeDateTime": "2021-07-21T11:13:23Z",
        "LastChangeTime": "11:13:23",
        "DangerousGoodsedProfile": "",
        "ProductDocumentChangeNumber": "1",
        "ProductDocumentPageCount": "1",
        "ProductDocumentPageNumber": "1",
        "DocumentIsCreatedByCAD": false,
        "ProductionOrspectionMemoTxt": "MEMO",
        "ProductionMemoPageFormat": "1",
        "ProductIsHighlyViscous": true,
        "TransportIsInBulk": true,
        "ProdEffctyParamValsAreAssigned": true,
        "ProdIsEnvironmentallyRelevant": true,
        "LaboratoryOrDesignOffice": "001",
        "PackagingProductGroup": "",
        "PackingReferenceProduct": "10050",
        "BasicProduct": "",
        "ProductDocumentNumber": "DOC",
        "ProductDocumentVersion": "1",
        "ProductDocumentType": "DMO",
        "ProductDocumentPageFormat": "1",
        "SAP__Messages": []
    }
    

### Error Reponse

 **Sample Code**

    {
    "error": {
    "code": "/IWBEP/CM_V4S_RUN/000",
    "message": "Unspecified provider error occurred. See Error Context and Call Stack.",
    "@SAP__common.ExceptionCategory": "Provider_Application_Error",
    "innererror": {
    "ErrorDetails": {
    "@SAP__common.Application": {
    "ComponentId": "BC-ESI-ESF-GW",
    "ServiceRepository": "SRVD_A2X",
    "ServiceId": "API_PRODUCT",
    "ServiceVersion": "0001"
    },
    "@SAP__common.TransactionId": "0A035BA921D204F0E0061495DC114D09",
    "@SAP__common.Timestamp": "20210921061706.637056",
    "@SAP__common.ErrorResolution": {
    "Analysis": "Use ADT feed reader \"SAP Gateway Error Log\" or run transaction /IWFND/ERROR_LOG on SAP Gateway hub system and search for entries with the timestamp above for more details",
    "Note": "See SAP Note 1797736 for error analysis (https://service.sap.com/sap/support/notes/1797736)"
    }
    }
    }
    }
    }

Product
=======

Technical name: Product

 **Note**

For this entity, SAP unit of measure is now language independent.

Properties
----------

ProductDocumentPageCount

Change Number's page count

Change Number

ProductDocumentPageNumber

Change Number's page number

Change Number

Product

Alphanumeric key uniquely identifying the product.

Mandatory

IsApprovedBatchRecordReqd

You use this indicator to specify that the following activities may only be performed after the relevant batch record has been approved:Alphanumeric key uniquely identifying the configurable product.

*   Making the usage decision for an inspection lot of the origin Goods receipt from production
    
*   Alphanumeric key uniquely identifying the configurableChanging the batch status from Restricted to Unrestricted
    

 **Note**

This operation is not supported in SAP S/4HANA Cloud Public Edition

Not Supported

ANPCode

Identifies the products that are controlled by the Brazilian Oil Agency.

Optional

ArticleCategory

Specifies the category of the product, for example, whether it is a single product, configurable product, or variant.

Optional

AuthorizationGroup

The authorization group enables you protect access to certain objects.

Optional

BaseISOUnit

ISO Code of the unit of measure in which stocks of the product are managed. The system converts all the quantities you enter in other units of measure (alternative units of measure) to the base unit of measure.

Optional

BaseUnit

Unit of measure in which stocks of the product are managed

Optional

BaseUnitSpecificProductHeight

Height of the product or its packaging, measured in the unit of dimension.

Optional

BaseUnitSpecificProductLength

Length of the product or its packaging, measured in the unit of dimension.

Optional

BaseUnitSpecificProductWidth

Width of the product or its packaging, measured in the unit of dimension.

Optional

BasicProduct

Basic constituent of the product.

Optional

CreatedByUser

Name of the person who created the record

Optional

CreationDate

Date on which the record was created

Optional

CreationDateTime

Date and time at which the record was created

Optional

CreationTime

Time at which the record was created

Optional

CrossPlantConfigurableProduct

Optional

CrossPlantStatus

Indicates whether the product may be used in the following areas for all plants: Materials management, Production planning and control, Plant maintenance and so on.

Optional

CrossPlantStatusValidityDate

Date from which the cross-plant product status is valid

Optional

DangerousGoodsedProfile

Alphanumeric key that uniquely identifies the dangerous goods profile.

Optional

DiscountInKindEligibility

Specifies whether and for what areas the product qualifies for a discount in kind. This indicator is presently used only in Purchasing.

Optional

Division

A way of grouping materials, products, or services

Optional

DocumentIsCreatedByCAD

This indicator shows that the object (such as BOM or document) was created or changed in a CAD system. Data transfer in the SAP system via CAD interface.

Optional

ExternalProductGroup

Key that can be used to assign the product to an external product group or to a product group determined according to external systematics.

Optional

GrossWeight

Gross weight expressed in the unit of weight specified by you in the Unit of weight field.

Optional

HandlingIndicator

Indicator that specifies how products are handled in the warehouse.

Optional

HandlingUnitType

Describes the handling unit type of a packaging product

Optional

HasVariableTareWeight

Flags all packaging materials for this packaging product type as packaging materials with a variable tare weight

Optional

IndustrySector

Key that specifies the branch of industry to which the product is assigned.

Optional

IndustryStandardName

Description of the product in accordance with the appropriate industry standard (such as ANSI or ISO).

Optional

InternationalArticleNumberCat

Category of International Article Number (EAN)

Optional

IsBatchManagementRequired

Specifies whether the product is managed in batches.

Optional

IsMarkedForDeletion

Indicator that allows you to flag a master record for deletion.

Optional

IsPilferable

Indicates that the product is pilferable, and possibly requires special storage in a secure storage type/section within the warehouse.

Optional

IsRelevantForHzdsSubstances

Indicates that there is hazardous substance data for this product.

Optional

ItemCategoryGroup

Products grouping that helps the system to determine item categories during sales document processing.

Optional

LaboratoryOrDesignOffice

Key for the design office, laboratory, or laboratory worker responsible.

Optional

LastChangeDate

Date on which the record was last changed.

Optional

LastChangeDateTime

Specifies the date and time at which the record was last changed

Optional

LastChangedByUser

Peron who changed the object last.

Optional

LastChangeTime

Specifies the time at which the record was last changed

Optional

ManufacturerNumber

Specifies the manufacturer of the manufacturer part number (MPN) product or the manufacturer's plant for which a manufacturer master record is created.

Optional

ManufacturerPartProfile

Specifies the process to work with the MPN products in the procurement process. The profile assigned then applies to all the MPN products that are assigned to this organization's own inventory-managed product.

Optional

MaximumCapacity

Maximum Allowed Capacity of Packaging Product

Optional

MaximumPackagingHeight

Maximum Packing Height of Packaging Product

Optional

MaximumPackagingLength

Maximum Packing Length of Packaging Product

Optional

MaximumPackagingWidth

Maximum Packing Width of Packaging Product

Optional

MaxPackggDimensionISOUnit

ISO Code for Unit of Measure for Maximum Packing Dimensions

Optional

NetWeight

Net weight expressed in the unit of weight specified by you in the Unit of weight field.

Optional

OvercapacityTolerance

Defines the tolerance limit for the maximum packaging capacity of a packaging product.

Optional

OwnInventoryManagedProduct

Number of the organization's own (internal) inventory-managed product

Optional

PackagingProductGroup

Groups together products that require similar packaging products.

Optional

PackingReferenceProduct

Products master record that serves as a template for packing with packing instructions for products that can be packed in the same way.

Optional

ProdAllocDetnProcedure

The product allocation determination procedure determines how product allocation is carried out.

The product allocation determination procedure should be entered in the basic data screen in the product master record.

Optional

ProdChmlCmplncRelevanceCode

Indicates whether the product is relevant for Compliance Monitor/Request for Compliance.

Optional

ProdCompetitorCustomerNumber

Customer number of the competitor. Competitors are managed in the SAP system as customers of a particular account group. This account group defines internally that the customer is a competitor.

You can store company, personnel, and any other data for each competitor.

The competitor number in the product master record serves to identify a competitive product as that of a particular commpetitor. Products can be contrasted and compared at different hierarchical levels thanks to this allocation of one's own products and competitive products to product groups.

Optional

ProdEffctyParamValsAreAssigned

Indicates whether you can assign values to the effectivity parameters or override the date, when you explode an assembly or a finished product.

Optional

ProdIsEnvironmentallyRelevant

Specifies that this is an environmentally relevant product.

Optional

ProductDocumentChangeNumber

Change Number

Optional

ProductDocumentNumber

Number of the drawing that exists for this object. Together with the document version, the document number is used as information for technical services. It is displayed in various lists.

Optional

ProductDocumentPageFormat

Page format of the internal technical document for this object.

Optional

ProductDocumentType

Subdivides the documents into groups that are subject to the same organizational processes. Together with the document number and the document version, the document type represents the key for document management. It is the main criterion for controlling document management. The document type controls field selection and the available statuses for a document info record.

Optional

ProductDocumentVersion

Version number of an in-house technical document for this object. Together with the document number, the document version is used as information for technical services. It is displayed on various lists.

Optional

ProductGroup

Key that is used to group together several products or services with the same attributes, and to assign them to a particular product group.

Optional

ProductHierarchy

Alphanumeric character string for grouping together materials by combining different characteristics. It is used for analyses and price determination.

In the standard SAP System, the product hierarchy can have up to 3 levels, each with a specific number of characters.

Optional

ProductionMemoPageFormat

Page format of the product's production or inspection memo.

Optional

ProductionOrInspectionMemoTxt

Number under which you have stored a production or inspection memo for the product.

Optional

ProductIsConfigurable

Indicator that determines whether the product is configurable.

Optional

ProductIsHighlyViscous

Indicator that shows if the product is a highly viscous substance. You use this indicator to control data output on transport documents.

Optional

ProductManufacturerNumber

Specifies the number, used by the manufacturer or by the supplier, to manage a product.

Optional

ProductMeasurementISOUnit

ISO Code for Unit of Dimension for Length/Width/Height

Optional

ProductMeasurementUnit

Unit of Dimension for Length/Width/Height

Optional

ProductOldID

Number under which you have managed the product so far or still manage it, for example, in aOptionalther system or in a card index.

Optional

ProductStandardID

A standardized unit that uniquely identifies a product relating to a unit of measure or type of packaging

Optional

ProductType

Product type defines certain attributes of the product and has important control functions.

Optional

ProductVolume

Space that the product occupies per unit of volume. The volume refers to the unit specified in the Volume unit field. Space that the product occupies per unit of volume. The volume refers to the unit specified in the Volume unit field.

Optional

QualityInspectionGroup

Quality Inspection Group

Optional

QuarantinePeriod

Numeric value indicating the period for quarantine. This value is read along with the unit of measure in the Time Unit for Quarantine Period field

Optional

QuarantinePeriodISOUnit

ISO Code for time unit of quarantine period

Optional

SerialNoExplicitnessLevel

Level on which the serial number must be unique.

Optional

SerialNumberProfile

Serial Number Profile

Optional

SizeOrDimensionText

Used to record the size or dimensions of the product

Optional

StandardHandlingUnitType

Describes the standard handling unit type for mixed handling units, where Optional packing instruction is used for creating the HU.

Optional

TimeUnitForQuarantinePeriod

Time Unit for Quarantine Period. For example, days, hours, weeks, and so on.

Optional

TransportIsInBulk

Indicator that shows if the dangerous goods are to be transported in bulk. You use this indicator to control data output (hazard identification number, for example) on transport documents.

Optional

UnitForMaxPackagingDimensions

Unit of Measure for Maximum Packing Length/Width/Height

Optional

VolumeISOUnit

ISO code of the unit referring to the volume of the product.

Optional

VolumeUnit

Unit referring to the volume of the product

Optional

WarehouseProductGroup

Groups products by warehousing points of view.

Optional

WarehouseStorageCondition

Describes the storage condition that should be used to store the product.

Optional

WeightISOUnit

ISO Code of the unit referring to the gross weight or net weight of the product.

Optional

WeightUnit

Unit referring to the gross weight or net weight of the product.

Optional