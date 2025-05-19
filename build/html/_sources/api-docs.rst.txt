API Documentation
==========================================================================

fetchSumStore Pinia Store


The `fetchSumStore` is a centralized Pinia store module used in a Quasar/Vue.js application. It manages user selections, indicator and table metadata, district geometry data, and interacts with both Supabase and GeoServer.

.. contents::
   :local:
   :depth: 2

Store ID
--------

- ``id``: ``fetchSumStore``

State Variables
---------------

.. list-table::
   :header-rows: 1

   * - Property
     - Type
     - Description
   * - userSelection
     - Object
     - Stores selected grantee, code, year, quota, etc.
   * - atYears
     - Object
     - Contains `at_year1` and `at_year2` for year comparisons.
   * - tableType
     - String
     - Type of table to display (e.g., ``ct``).
   * - currentTab
     - String
     - Current tab selected in the UI (e.g., ``pirs``).
   * - sumsTab
     - String
     - Sub-tab under `sums` context.
   * - sumsIndicators
     - Array or null
     - Stores fetched sum indicator codes from Supabase.
   * - faIndicators
     - Array or null
     - Stores fetched FA indicator mappings from Supabase.
   * - selectedGrantee
     - String
     - User-selected grantee.
   * - selectedIndicatorCode
     - String
     - Selected indicator code.
   * - selectedYear
     - String
     - Year selected by the user.
   * - selectedQuota
     - String
     - Quarter or period selected (e.g., ``janmar``).
   * - districts
     - Object or null
     - Stores district GeoJSON data.
   * - ctTable
     - Object or null
     - Stores current CT table data.

Getters
-------

.. list-table::
   :header-rows: 1

   * - Getter Name
     - Returns
     - Description
   * - getCurrentTab
     - String
     - Current selected tab.
   * - getUserSelection
     - Object
     - Full `userSelection` object.
   * - getSumsIndicators
     - Array or null
     - Returns `sumsIndicators`.
   * - getfaIndicators
     - Array or null
     - Returns `faIndicators`.
   * - getSelectedGrantee
     - String
     - Returns selected grantee.
   * - getSelectedYear
     - String
     - Returns selected year.
   * - getSelectedQuota
     - String
     - Returns selected quarter.
   * - getSelectedTable
     - String
     - Returns selected table type.
   * - getctTable
     - Object or null
     - Returns CT table data.
   * - getAtYear
     - Object
     - Returns the year comparison object.
   * - getSumsTab
     - String
     - Returns selected `sumsTab`.

Actions
-------

District Data
~~~~~~~~~~~~~

.. function:: fetchDistrictData()

   Fetches GeoJSON features from `agriconnect:Districts` via WFS.

   - **Sets**: ``districts`` (full axios response)
   - **Source**: GeoServer WFS

.. function:: setDistrictData()

   Fetches a subset (max 50 features) of `agriconnect:OP_DISTRICTS`.

   - **Sets**: ``districts`` (parsed GeoJSON)
   - **Source**: GeoServer WFS

Supabase Data
~~~~~~~~~~~~~

.. function:: fetchSumsIndicators()

   Loads all records from the `codes_sums_indicators` table in Supabase.

   - **Sets**: ``sumsIndicators``

.. function:: fetchfaIndicators()

   Loads `id`, `sumsstopgapcode`, and `faindicators` from `codes_fa_indicators`.

   - **Sets**: ``faIndicators``

User Selections
~~~~~~~~~~~~~~~

.. function:: setCurrentTab(value)
   :param value: string

   Updates the UI's main tab.

.. function:: setTableType(value)

.. function:: setSelectedIndicatorCode(value)

.. function:: setSelectedfaIndicatorCode(value)

.. function:: setSelectedGrantee(value)

.. function:: setSelectedfaGrantee(value)

.. function:: setSelectedYear(value)

.. function:: setSelectedQuota(value)

.. function:: setSelectedAggregate(value)

.. function:: setDefaultUserSelection(value)

   - Accepts an object `{ year, aggregate }`.

Table and Year State
~~~~~~~~~~~~~~~~~~~~

.. function:: setCTtable(value)

.. function:: setATyears(value)

.. function:: setSumsTab(value)

Dependencies
------------

- **Supabase**: For interacting with `codes_sums_indicators` and `codes_fa_indicators`.
- **GeoServer WFS**: Used for loading district data (`agriconnect:Districts`, `agriconnect:OP_DISTRICTS`).
- **Axios**: Handles WFS HTTP GET requests.

Notes
-----

- Errors from Supabase are logged to the browser console.
- `fetchDistrictData()` stores the full axios response; `setDistrictData()` parses the `.data` field.
