# ODS Widgets Documentation

**Total Widgets:** 67

---

### odsAdvAnalysis

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsAdvAnalysis widget exposes the results of an aggregation function over a context. It uses the ODS Explore API V2.1 and its [ODSQL language](https://help.huwise.com/apis/ods-explore-v2/#section/Opendatasoft-Query-Language-%28ODSQL%29), which offers greater flexibility than the v1.

The parameters for this widgets are dynamic, which implies two benefits:

  * First, changes in context parameters will refresh the results of the widget.
  * Second, AngularJS variables are accepted as attributes.



The results can then be displayed in three different ways:

  * To create specific visualizations, using custom-made HTML and CSS
  * A table view is also available using `odsAdvTable` (examples are provided below).
  * As the widget is creating an AngularJS variable, it can be displayed through a simple `{{myData.results[X]}}`. This usage is not documented here, as it regards HTML code and widgets already documented in [the introduction](https://help.huwise.com/widgets/#/introduction/).



For retro-compatibility purposes, similarly to API V2.0, if the `groupBy` is done on a field that contains null values, they will be removed. If you are using the `limit` parameter, this may cause the widget to return one less category as expected, because the null group was included. You can prevent this by using `where` to exclude null values from this field, using `IS NOT NULL` (e.g. `my_field IS NOT NULL`).

#### Examples of requests to make

How to compute a weighted average:

In this example, the widget will return the average height of the trees according to the population size of each species in Paris districts. 
      
      1. <ods-dataset-context
        2.     context="ctx"
        3.     ctx-domain="https://documentation-resources.huwise.com/"
        4.     ctx-dataset="les-arbres-remarquables-de-paris">
        5.     <div ods-adv-analysis="myData"
        6.         ods-adv-analysis-context="ctx"
        7.         ods-adv-analysis-select="(sum(hauteur_en_m)/count(espece)) as y_axis"
        8.         ods-adv-analysis-where="arrondissement LIKE 'paris'"
        9.         ods-adv-analysis-group-by="espece as x_axis">
        10.         {{myData}}
        11.     </div>
        12. </ods-dataset-context>
    
    

How to create multiple time series:

In this example, the widget returns the average gold price by month in 2018 and 2019. The `group-by` year allows to compare each year with the others. 
      
      1. <ods-dataset-context
        2.     context="ctx"
        3.     ctx-domain="https://documentation-resources.huwise.com/"
        4.     ctx-dataset="gold-prices">
        5.     <div ods-adv-analysis="myData"
        6.         ods-adv-analysis-context="ctx"
        7.         ods-adv-analysis-select="avg(price) as y_axis"
        8.         ods-adv-analysis-where="date > date'2017'"
        9.         ods-adv-analysis-group-by="month(date) as x_axis, year(date) as series">
        10.         {{myData}}
        11.     </div>
        12. </ods-dataset-context>
    
    

#### How to use odsAdvancedAnalysis with odsAdvTable

**odsAdvancedTable** was designed to accept the JSON created by **odsAdvancedAnalysis**. Its purpose is to offer a table view that matches the widget and to provide an accessible way of displaying data as an alternative to charts.

For more information, see the documentation for odsAdvTable. 
      
      1. <ods-dataset-context
        2.     context="ctx"
        3.     ctx-domain="https://documentation-resources.huwise.com/"
        4.     ctx-dataset="les-arbres-remarquables-de-paris">
        5.     <div ods-adv-analysis="myData"
        6.         ods-adv-analysis-context="ctx"
        7.         ods-adv-analysis-select="count(objectid) as quantite_arbres, AVG(circonference_en_cm) as circonference_moyenne"
        8.         ods-adv-analysis-group-by="arrondissement">
        9.         <ods-adv-table
        10.             data="myData"
        11.             sticky-header="true"
        12.             sticky-first-column="true"
        13.             columns-order="['arrondissement', 'quantite_arbres', 'circonference_moyenne']"
        14.             totals="['quantite_arbres']"
        15.             sort="arrondissement ASC">
        16.         </ods-adv-table>
        17.     </div>
        18. </ods-dataset-context>
    
    


#### Usage

as attribute
      
      1. <ANY ods-adv-analysis="{string}"
        2.      ods-adv-analysis-context="{string}"
        3.      [ods-adv-analysis-select]="{string}"
        4.      [ods-adv-analysis-where]="{string}"
        5.      [ods-adv-analysis-group-by]="{string}"
        6.      [ods-adv-analysis-order-by]="{string}"
        7.      [ods-adv-analysis-limit]="{string}">
        8.    ...
        9. </ANY>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
odsAdvAnalysis| [string]()| This name can be used as the `data` attribute of the display widgets that support it (e.g. `odsAdvTable`).  
odsAdvAnalysisContext| [string]()| Insert here the name of the context to use.  
[odsAdvAnalysisSelect]| [string]()| Type here the query to make. More use cases are available below. The documentation about the ODSQL select clause is available here. This clause will contain the values (i.e., the y-axis in case of a chart).  
[odsAdvAnalysisWhere]| [string]()| This parameter allows to filter rows with a combination of expressions. The documentation about the ODSQL `where` clause is available [here](https://help.huwise.com/apis/ods-explore-v2/#section/Opendatasoft-Query-Language-%28ODSQL%29/Where-clause).  
[odsAdvAnalysisGroupBy]| [string]()| This parameter helps regroup the calculation according to specific criteria. The `group-by` in this clause can become either y-axis or series in a chart. The documentation about the ODSQL `GROUP BY` clause is available [here](https://help.huwise.com/apis/ods-explore-v2/#section/Opendatasoft-Query-Language-%28ODSQL%29/Group-by-clause).  
[odsAdvAnalysisOrderBy]| [string]()| This parameter is used to sort the results of an aggregation using the `ASC` and `DESC` keywords (e.g., `myField ASC` or ). The documentation about the ODSQL `ORDER BY` clause is available [here](https://help.huwise.com/apis/ods-explore-v2/#section/Opendatasoft-Query-Language-%28ODSQL%29/Order-by-clause).  
[odsAdvAnalysisLimit]| [string]()| Limits the number of items to return.


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| odsAdvAnalysis | string | This name can be used as thedataattribute of the display widgets that support it (e.g.odsAdvTable). |
| odsAdvAnalysisContext | string | Insert here the name of the context to use. |
| [odsAdvAnalysisSelect] | string | Type here the query to make. More use cases are available below. The documentation about the ODSQL select clause is available here. This clause will contain the values (i.e., the y-axis in case of a chart). |
| [odsAdvAnalysisWhere] | string | This parameter allows to filter rows with a combination of expressions. The documentation about the ODSQLwhereclause is availablehere. |
| [odsAdvAnalysisGroupBy] | string | This parameter helps regroup the calculation according to specific criteria. Thegroup-byin this clause can become either y-axis or series in a chart. The documentation about the ODSQLGROUP BYclause is availablehere. |
| [odsAdvAnalysisOrderBy] | string | This parameter is used to sort the results of an aggregation using theASCandDESCkeywords (e.g.,myField ASCor ). The documentation about the ODSQLORDER BYclause is availablehere. |
| [odsAdvAnalysisLimit] | string | Limits the number of items to return. |

---
### odsAdvTable

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsAdvTable widget is used to analyze data from a table perspective.

It is especially interesting to use this widget in conjunction with an odsAdvAnalysis widget, but you can feed it with static data. The odsAdvTable widget gives you the ability to:

  * compute totals,
  * sort, reorder and rename columns,
  * format numbers as text and define the number of decimal places to round the number to, and
  * set the header and/or the first column in a fixed position.




#### Usage

as element:
      
      1. <ods-adv-table
        2.        data="{array}"
        3.        [columns-order]="{array}"
        4.        [columns-options]="{object}"
        5.        [sort]="{string}"
        6.        [totals]="{array}"
        7.        sticky-header="{boolean}"
        8.        sticky-first-column="{boolean}">
        9. </ods-adv-table>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
data| [array]()| The input array of value which feeds the table.  
[columnsOrder]| [array]()| An array of strings representing the columns' order.  
[columnsOptions]| [object]()| An object representing the formatting to apply on the columns. Two options are available: `label` is used to rename the column's header and `decimals` to set the number of decimals on each cell of the column (e.g., `{ label: 'New name', decimals: 2 }`).  
[sort]| [string]()| Name of the column to sort on, following by the suffix `ASC` or `DESC` (e.g., `columnName ASC`).  
[totals]| [array]()| An array of strings containing the names of the columns whose totals must be calculated.  
stickyHeader| [boolean]()| When set to `true`, the header will be fixed at the top of the table. _(default: false)_  
stickyFirstColumn| [boolean]()| When set to `true`, the first column will be fixed on the left side of the table. _(default: false)_


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| data | array | The input array of value which feeds the table. |
| [columnsOrder] | array | An array of strings representing the columns' order. |
| [columnsOptions] | object | An object representing the formatting to apply on the columns. Two options are available:labelis used to rename the column's header anddecimalsto set the number of decimals on each cell of the column (e.g.,{ label: 'New name', decimals: 2 }). |
| [sort] | string | Name of the column to sort on, following by the suffixASCorDESC(e.g.,columnName ASC). |
| [totals] | array | An array of strings containing the names of the columns whose totals must be calculated. |
| stickyHeader | boolean | When set totrue, the header will be fixed at the top of the table.(default: false) |
| stickyFirstColumn | boolean | When set totrue, the first column will be fixed on the left side of the table.(default: false) |

---
### odsAggregation

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsAggregation widget creates a variable that contains the result of an aggregation function based on a context.

Aggregations are functions that enable to group records and compute statistical values for numeric fields. For instance, aggregations can determine, based on several records, the smallest or biggest value among them, compute the average value or count the number of values for a chosen field.

odsAggregation supports multiple declarations of aggregations.


#### Usage

as attribute
      
      1. <ANY ods-aggregation="{string}"
        2.      ods-aggregation-context="{DatasetContext}"
        3.      ods-aggregation[-variablename]-context="{DatasetContext}"
        4.      ods-aggregation-function="{string}"
        5.      ods-aggregation[-variablename]-function="{string}"
        6.      ods-aggregation-expression="{string}"
        7.      ods-aggregation[-variablename]-expression="{string}">
        8.    ...
        9. </ANY>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
odsAggregation| [string]()|  _(mandatory)_ Name of the variable that holds the result of the aggregation. For multiple aggregations, variable names must be separated with commas. _(default: aggregation)_  
odsAggregationContext| [DatasetContext]()|  _(mandatory)_ Dataset Context to use.  
odsAggregation[Variablename]Context| [DatasetContext]()| Context specific to the `[Variablename]` aggregation. `[Variablename]` must be replaced with the name of the variable, declared through the **odsAggregation** parameter.  
odsAggregationFunction| [string]()|  _(mandatory)_ Aggregation function to apply:

  * AVG: average
  * COUNT
  * MIN: minimum
  * MAX: maximum
  * STDDEV: standard deviation
  * SUM

_(default: COUNT)_  
odsAggregation[Variablename]Function| [string]()| Function specific to the `[Variablename]` aggregation. `[Variablename]` must be replaced with the name of the variable, declared through the **odsAggregation** parameter. _(default: COUNT)_  
odsAggregationExpression| [string]()|  _(optional only with the COUNT function)_ Expression to apply the function on (e.g., the name of a field). _(default: none)_  
odsAggregation[Variablename]Expression| [string]()| Expression specific to the `[Variablename]` aggregation. `[Variablename]` must be replaced with the name of the variable, declared through the **odsAggregation** parameter. _(default: none)_


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| odsAggregation | string | (mandatory)Name of the variable that holds the result of the aggregation. For multiple aggregations, variable names must be separated with commas.(default: aggregation) |
| odsAggregationContext | DatasetContext | (mandatory)Dataset Contextto use. |
| odsAggregation[Variablename]Context | DatasetContext | Context specific to the[Variablename]aggregation.[Variablename]must be replaced with the name of the variable, declared through theodsAggregationparameter. |
| odsAggregationFunction | string | (mandatory)Aggregation function to apply:AVG: averageCOUNTMIN: minimumMAX: maximumSTDDEV: standard deviationSUM(default: COUNT) |
| odsAggregation[Variablename]Function | string | Function specific to the[Variablename]aggregation.[Variablename]must be replaced with the name of the variable, declared through theodsAggregationparameter.(default: COUNT) |
| odsAggregationExpression | string | (optional only with the COUNT function)Expression to apply the function on (e.g., the name of a field).(default: none) |
| odsAggregation[Variablename]Expression | string | Expression specific to the[Variablename]aggregation.[Variablename]must be replaced with the name of the variable, declared through theodsAggregationparameter.(default: none) |

---
### odsAnalysis

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsAnalysis widget creates a variable that contains the result of an analysis (i.e., an object containing a results array and optionally an aggregations object).

odsAnalysis allows applying functions to chosen groups of data to analyze them with the same logic as a chart visualization. For instance, an analysis can obtain the average value for several data series, broken down by a chosen field used as an X-axis. The result can then be sorted by another series.

odsAnalysis can be used with the AngularJS ngRepeat directive to build a table of analysis results.


#### Usage

as attribute
      
      1. <ANY ods-analysis="{string}"
        2.      ods-analysis-context="{DatasetContext}"
        3.      ods-analysis-max="{number}"
        4.      ods-analysis-x="{string}"
        5.      ods-analysis-sort="{string}"
        6.      ods-analysis-serie-name="{string}">
        7.    ...
        8. </ANY>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
odsAnalysis| [string]()|  _(mandatory)_ Name of the variable _(default: analysis)_  
odsAnalysisContext| [DatasetContext]()|  _(mandatory)_ Dataset Context to use.  
odsAnalysisMax| [number]()| Maximum number of results to show. _(default: all)_  
odsAnalysisX| [string]()| Name of the field used as X-axis (e.g., date or datetime field, facet, etc.) _(default: none)_  
odsAnalysisSort| [string]()| Name of the series to sort on. Note that `-` before the name of the series indicates that the sorting will be descending instead of ascending (e.g., `-serieName`). _(default: none)_  
odsAnalysisSerieName| [string]()| Function to apply:

  * AVG: average
  * COUNT
  * MIN: minimum
  * MAX: maximum
  * STDDEV: standard deviation
  * SUM

Must be written in the following form: `FUNCTION(fieldname)`. _(default: none)_


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| odsAnalysis | string | (mandatory)Name of the variable(default: analysis) |
| odsAnalysisContext | DatasetContext | (mandatory)Dataset Contextto use. |
| odsAnalysisMax | number | Maximum number of results to show.(default: all) |
| odsAnalysisX | string | Name of the field used as X-axis (e.g., date or datetime field, facet, etc.)(default: none) |
| odsAnalysisSort | string | Name of the series to sort on.Note that-before the name of the series indicates that the sorting will be descending instead of ascending (e.g.,-serieName).(default: none) |
| odsAnalysisSerieName | string | Function to apply:AVG: averageCOUNTMIN: minimumMAX: maximumSTDDEV: standard deviationSUMMust be written in the following form:FUNCTION(fieldname).(default: none) |

---
### odsAutoResize

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsAutoResize widget enables the auto-resize functionality on a widget that supports it. By default, this widget forces the affected element to fill the height to the bottom of the window.


#### Usage

as attribute
      
      1. <ANY ods-auto-resize>
        2.    ...
        3. </ANY>
    
    


---
### odsCalendar

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsCalendar widget can take any dataset containing at least two datetime fields and a text field and use it to display a calendar. It can load at most 1000 events (records) at once.


#### Usage

as element:
      
      1. <ods-calendar
        2.        context="{DatasetContext}"
        3.        start-field="{string}"
        4.        end-field="{string}"
        5.        title-field="{string}"
        6.        event-color="{string}"
        7.        tooltip-fields="{string}"
        8.        calendar-view="{string}"
        9.        available-calendar-views="{string}"
        10.        [sync-to-url]="{boolean}">
        11. </ods-calendar>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
context| [DatasetContext]()| Dataset Context to use  
startField| [string]()| The name of the datetime field to use as event start datetime  
endField| [string]()| The name of the datetime field to use as event end datetime  
titleField| [string]()| The name of the text field to use as event title  
eventColor| [string]()| The color (in hexadecimal form) used for all events _(default: #C32D1C)_  
tooltipFields| [string]()| An ordered, comma-separated list of fields to display in the event tooltip _(default: none)_  
calendarView| [string]()| The default mode for the calendar. The authorized values are 'month', 'agendaWeek', and 'agendaDay'. _(default: month)_  
availableCalendarViews| [string]()| A comma-separated list of available views for the calendar. It must be a sub list of ['month', 'agendaWeek', 'agendaDay']. _(default: 'month','agendaWeek','agendaDay')_  
[syncToUrl]| [boolean]()| When set to `true`, it persists the `calendarView` in the page URL.


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| context | DatasetContext | Dataset Contextto use |
| startField | string | The name of the datetime field to use as event start datetime |
| endField | string | The name of the datetime field to use as event end datetime |
| titleField | string | The name of the text field to use as event title |
| eventColor | string | The color (in hexadecimal form) used for all events(default: #C32D1C) |
| tooltipFields | string | An ordered, comma-separated list of fields to display in the event tooltip(default: none) |
| calendarView | string | The default mode for the calendar. The authorized values are 'month', 'agendaWeek', and 'agendaDay'.(default: month) |
| availableCalendarViews | string | A comma-separated list of available views for the calendar. It must be a sub list of ['month', 'agendaWeek', 'agendaDay'].(default: 'month','agendaWeek','agendaDay') |
| [syncToUrl] | boolean | When set totrue, it persists thecalendarViewin the page URL. |

---
### odsCatalogContext

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsCatalogContext widget represents the entire catalog of datasets of a chosen domain and a set of parameters used to query this catalog. One or more widgets can use a catalog context: it allows them to share information (i.e., the query parameters).

For example, a widget that displays a time filter (odsTimerange) can be plugged into the same context as a results list (odsResultEnumerator) so that the user can filter the displayed results.

odsCatalogContext creates a new child scope, within which its declared contexts are available for any other widget used inside that odsCatalogContext element. odsCatalogContext widgets can also be nested inside each other.

A single odsCatalogContext can declare one or several contexts, which are initialized when declared through the **context** parameter. Each context is configured using parameters prefixed by the context name (`contextname-setting`, e.g., mycontext-domain).

**Properties of odsCatalogContext used as variable**

Once created, the context is accessible as a variable named after it. The context contains properties that can be accessed directly:

  * `domainUrl`: full URL of the domain of the context that can be used to create links
  * `parameters`: parameters object of the context




#### Usage

as element:
      
      1. <ods-catalog-context
        2.        context="{string}"
        3.        domain="{string}"
        4.        apikey="{string}"
        5.        parameters="{object}"
        6.        url-sync="{boolean}">
        7. </ods-catalog-context>
    
    

as attribute
      
      1. <ANY ods-catalog-context
        2.      context="{string}"
        3.      domain="{string}"
        4.      apikey="{string}"
        5.      parameters="{object}"
        6.      url-sync="{boolean}">
        7.    ...
        8. </ANY>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
context| [string]()|  _(mandatory)_ Name, or list of names separated by commas, of context(s) to declare. Context names must be in lowercase, can only contain alphanumerical characters, and cannot begin with a number, "data", or "x".  
domain| [string]()| Domain where the dataset(s) can be found. Since the domain value is used to construct an URL to an API root, it can be:

  * an alphanumeric string (e.g., _mydomain_): it will assume that it is a Huwise domain (e.g., _mydomain.huwise.com_)
  * a hostname (e.g., _data.mydomain.com_)
  * a relative path (e.g., _/monitoring_): it will be relative to the hostname of the current page
  * a hostname and a path (e.g., _data.mydomain.com/monitoring_)

By default, if the domain parameter is not set, ODSWidgetsConfig.defaultDomain is used. _(default: ODSWidgetsConfig.defaultDomain)_  
apikey| [string]()| API key to use in every API call for the context. For more information, see [Generating an API key](https://userguide.huwise.com/en/articles/2044226)). _(default: none)_  
parameters| [object]()| Object holding parameters to apply to the context when it is created _(default: none)_  
urlSync| [boolean]()| Enables synchronization of the parameters to the page's parameters (query string). When sharing the page with parameters in the URL, the context will use them; and if the context parameters change, the URL parameters will change as well. Note that if this parameter is enabled, `parameters` and `parametersFromContext` won't have any effect. There can also only be a single context with URL synchronization enabled, else the behavior will be unpredictable. _(default: none)_


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| context | string | (mandatory)Name, or list of names separated by commas, of context(s) to declare. Context names must be in lowercase, can only contain alphanumerical characters, and cannot begin with a number, "data", or "x". |
| domain | string | Domain where the dataset(s) can be found. Since the domain value is used to construct an URL to an API root, it can be:an alphanumeric string (e.g.,mydomain): it will assume that it is a Huwise domain (e.g.,mydomain.huwise.com)a hostname (e.g.,data.mydomain.com)a relative path (e.g.,/monitoring): it will be relative to the hostname of the current pagea hostname and a path (e.g.,data.mydomain.com/monitoring)By default, if the domain parameter is not set,ODSWidgetsConfig.defaultDomainis used.(default: ODSWidgetsConfig.defaultDomain) |
| apikey | string | API key to use in every API call for the context. For more information, seeGenerating an API key).(default: none) |
| parameters | object | Object holding parameters to apply to the context when it is created(default: none) |
| urlSync | boolean | Enables synchronization of the parameters to the page's parameters (query string). When sharing the page with parameters in the URL, the context will use them; and if the context parameters change, the URL parameters will change as well. Note that if this parameter is enabled,parametersandparametersFromContextwon't have any effect. There can also only be a single context with URL synchronization enabled, else the behavior will be unpredictable.(default: none) |

---
### odsChart

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsChart widget is the base widget allowing to display charts from Huwise datasets. A Chart is defined by one or more series that get their data from form one or more datasets represented by a Dataset Context, a type of chart, and multiple parameters to fine-tune the chart's appearance.

Note: `min` and `max` parameters are dynamic, which means that if they change, the chart will be refreshed accordingly.

Basic example: 
      
      1. <ods-dataset-context context="trees"
        2.                      trees-dataset="les-arbres-remarquables-de-paris"
        3.                      trees-domain="documentation-resources">
        4.     <ods-chart>
        5.         <ods-chart-query context="trees" field-x="espece" maxpoints="10">
        6.             <ods-chart-serie expression-y="circonference_en_cm" chart-type="column" function-y="MAX" color="#66c2a5">
        7.             </ods-chart-serie>
        8.         </ods-chart-query>
        9.     </ods-chart>
        10. </ods-dataset-context>
    
    

You can display multiple series from the same dataset on the same chart: 
      
      1. <ods-dataset-context context="trees"
        2.                      trees-dataset="les-arbres-remarquables-de-paris"
        3.                      trees-domain="documentation-resources">
        4.     <ods-chart>
        5.         <ods-chart-query context="trees" field-x="espece" maxpoints="10">
        6.             <ods-chart-serie expression-y="circonference_en_cm" chart-type="column" function-y="AVG" color="#66c2a5">
        7.             </ods-chart-serie>
        8.             <ods-chart-serie expression-y="hauteur_en_m" chart-type="column" function-y="AVG" color="#fc8d62">
        9.             </ods-chart-serie>
        10.         </ods-chart-query>
        11.     </ods-chart>
        12. </ods-dataset-context>
    
    

You can display multiple series from multiple datasets on the same chart: 
      
      1. <ods-dataset-context context="commute,demographics"
        2.                      commute-dataset="commute-time-us-counties"
        3.                      commute-domain="https://documentation-resources.huwise.com/"
        4.                      demographics-dataset="us-cities-demographics"
        5.                      demographics-domain="https://documentation-resources.huwise.com/">
        6.     <ods-chart align-month="true">
        7.         <ods-chart-query context="commute" field-x="state" maxpoints="20">
        8.             <ods-chart-serie expression-y="mean_commuting_time" chart-type="column" function-y="AVG" color="#66c2a5" scientific-display="true">
        9.             </ods-chart-serie>
        10.         </ods-chart-query>
        11.         <ods-chart-query context="demographics" field-x="state" maxpoints="20">
        12.             <ods-chart-serie expression-y="count" chart-type="column" function-y="SUM" color="#fc8d62" scientific-display="true">
        13.             </ods-chart-serie>
        14.         </ods-chart-query>
        15.     </ods-chart>
        16. </ods-dataset-context>
    
    


#### Usage

as element:
      
      1. <ods-chart
        2.        timescale="{string}"
        3.        label-x="{string}"
        4.        single-y-axis="{boolean}"
        5.        single-y-axis-label="{string}"
        6.        min="{integer}"
        7.        max="{integer}"
        8.        step="{integer}"
        9.        scientific-display="{boolean}"
        10.        logarithmic="{boolean}"
        11.        display-legend="{boolean}"
        12.        align-month="{boolean}"
        13.        labels-x-length="{integer}">
        14. </ods-chart>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
timescale| [string]()| Works only with timeseries. If it defines the default timescale to use to display the X-axis. It does not affect how the different series are requested (they have their own timescale) but enforces X-axis intervals. _(default: none)_  
labelX| [string]()| If set, it overrides the default X-axis label. The default label is generated from the series. _(default: none)_  
singleYAxis| [boolean]()| Enforces the use of only one Y-axis for all series. In this case, specific Y-axis parameters defined for each series will be ignored. _(default: false)_  
singleYAxisLabel| [string]()| Sets the label for the single Y-axis.  
min| [integer]()| Sets the min displayed value for Y-axis. Active only when singleYAxis is true. _(default: null)_  
max| [integer]()| Sets the max displayed value for Y-axis. Active only when singleYAxis is true. _(default: null)_  
step| [integer]()| Specifies the step between each tick on the Y axis. If not defined, it is computed automatically. Active only when singleYAxis is true. _(default: null)_  
scientificDisplay| [boolean]()| When set to false, force the full display of the numbers on the Y-axis. Active only when singleYAxis is true. _(default: true)_  
logarithmic| [boolean]()| Uses a logarithmic scale for Y-axis. Active only when singleYAxis is true. _(default: false)_  
displayLegend| [boolean]()| Enables or disables the display of series legend. Active only when singleYAxis is true. _(default: true)_  
alignMonth| [boolean]()| Aligns the month values with the month label. The old behavior aligns values with the middle of the month. Setting this parameter to false reverts to the old behavior. _(default: true)_  
labelsXLength| [integer]()| Sets the maximum number of characters displayed for the X-axis labels. _(default: 12)_


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| timescale | string | Works only with timeseries. If it defines the default timescale to use to display the X-axis. It does not affect how the different series are requested (they have their own timescale) but enforces X-axis intervals.(default: none) |
| labelX | string | If set, it overrides the default X-axis label. The default label is generated from the series.(default: none) |
| singleYAxis | boolean | Enforces the use of only one Y-axis for all series. In this case, specific Y-axis parameters defined for each series will be ignored.(default: false) |
| singleYAxisLabel | string | Sets the label for the single Y-axis. |
| min | integer | Sets the min displayed value for Y-axis. Active only when singleYAxis is true.(default: null) |
| max | integer | Sets the max displayed value for Y-axis. Active only when singleYAxis is true.(default: null) |
| step | integer | Specifies the step between each tick on the Y axis. If not defined, it is computed automatically. Active only when singleYAxis is true.(default: null) |
| scientificDisplay | boolean | When set to false, force the full display of the numbers on the Y-axis. Active only when singleYAxis is true.(default: true) |
| logarithmic | boolean | Uses a logarithmic scale for Y-axis. Active only when singleYAxis is true.(default: false) |
| displayLegend | boolean | Enables or disables the display of series legend. Active only when singleYAxis is true.(default: true) |
| alignMonth | boolean | Aligns the month values with the month label. The old behavior aligns values with the middle of the month. Setting this parameter to false reverts to the old behavior.(default: true) |
| labelsXLength | integer | Sets the maximum number of characters displayed for the X-axis labels.(default: 12) |

---
### odsChartQuery

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsChartQuery widget is the sub widget that defines the queries for the series defined inside. For complete examples, see odsChart.

Note: All parameters are dynamic, which means that if they change, the chart will be refreshed accordingly.


#### Usage

as element:
      
      1. <ods-chart-query
        2.        field-x="{string}"
        3.        timescale="{string}"
        4.        maxpoints="{integer}"
        5.        stacked="{string}"
        6.        reverse-stacks="{boolean}"
        7.        series-breakdown="{string}"
        8.        series-breakdown-timescale="{string}"
        9.        category-colors="{object}"
        10.        sort="{string}">
        11. </ods-chart-query>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
fieldX| [string]()| Sets the field that is used to compute the aggregations during the analysis query.  
timescale| [string]()| Works only with timeseries (when fieldX is a date or datetime). Y values will be computed against this interval. For example, if you have daily values in a dataset and ask for a "month" timescale, the Y values for the series inside this query will aggregated month by month and computed. _(default: "year")_  
maxpoints| [integer]()| Defines the maximum number of points fetched by the query. With a value of 0, all points will be fetched by the query. _(default: 50)_  
stacked| [string]()| Stacks the resulting charts. Stacked values can 'normal' or 'percent'. Only works with columns, bar, line, spline, area, and spline area charts. _(default: null)_  
reverseStacks| [boolean]()| Reverses the order of the displayed stack. Only works with stacked charts when the singleYAxis option is not active on the chart. _(default: false)_  
seriesBreakdown| [string]()| When declared, all series are broken down by the defined facet. _(default: none)_  
seriesBreakdownTimescale| [string]()| If the breakdown facet is a time serie (date or datetime), it defines the aggregation level for this facet. _(default: true)_  
categoryColors| [object]()| A object containing a color for each category name. For example: {'my value': '#FF0000', 'my other value': '#0000FF'} _(default: {})_  
sort| [string]()| Displays the results in a specific order. The following values are available:

  * To sort based on horizontal axis, use `x` or `-x`. For date-based axes, you need to include the name of the field, and the highest precision in the displayed data. For example, if the field name is `mydate`, and the data includes the year, you can use `x.mydate.year`.
  * To sort based on the displayed values, use `y` or `-y` if there is a single serie. If there are multiple series, use `series{n}-{m}` where `n` is the {n}th `ods-chart-query`, and m is the {m}th `ods-chart-serie`

_(default: none)_


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| fieldX | string | Sets the field that is used to compute the aggregations during the analysis query. |
| timescale | string | Works only with timeseries (when fieldX is a date or datetime). Y values will be computed against this interval. For example, if you have daily values in a dataset and ask for a "month" timescale, the Y values for theseriesinside this query will aggregated month by month and computed.(default: "year") |
| maxpoints | integer | Defines the maximum number of points fetched by the query. With a value of 0, all points will be fetched by the query.(default: 50) |
| stacked | string | Stacks the resulting charts. Stacked values can 'normal' or 'percent'. Only works with columns, bar, line, spline, area, and spline area charts.(default: null) |
| reverseStacks | boolean | Reverses the order of the displayed stack. Only works with stacked charts when the singleYAxis option is not active on the chart.(default: false) |
| seriesBreakdown | string | When declared, all series are broken down by the defined facet.(default: none) |
| seriesBreakdownTimescale | string | If the breakdown facet is a time serie (date or datetime), it defines the aggregation level for this facet.(default: true) |
| categoryColors | object | A object containing a color for each category name. For example: {'my value': '#FF0000', 'my other value': '#0000FF'}(default: {}) |
| sort | string | Displays the results in a specific order. The following values are available:To sort based on horizontal axis, usexor-x. For date-based axes, you need to include the name of the field, and the highest precision in the displayed data. For example, if the field name ismydate, and the data includes the year, you can usex.mydate.year.To sort based on the displayed values, useyor-yif there is a single serie. If there are multiple series, useseries{n}-{m}wherenis the {n}thods-chart-query, and m is the {m}thods-chart-serie(default: none) |

---
### odsChartSerie

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsChartSerie widget is the sub widget that defines a series in the chart with all its parameters. For complete examples, see odsChart.

### Available chart types:

There are two available types of charts: simple series and areas that take a minimal and a maximal value.

#### Simple series

  * line
  * spline
  * area
  * areaspline
  * column
  * bar
  * pie
  * scatter
  * polar
  * spiderweb
  * funnel



#### Areas

  * arearange
  * areasplinerange
  * columnrange



### Available functions

  * COUNT
  * AVG
  * MIN
  * MAX
  * STDDEV
  * SUM
  * QUANTILES
  * CONSTANT




#### Usage

as element:
      
      1. <ods-chart-serie
        2.        [chart-type]="{string}"
        3.        [function-y]="{string}"
        4.        [expression-y]="{string}"
        5.        [color]="{string}"
        6.        [label-y]="{string}"
        7.        labelsposition="{string}"
        8.        innersize="{number}"
        9.        [cumulative]="{boolean}"
        10.        logarithmic="{boolean}"
        11.        min="{integer}"
        12.        max="{integer}"
        13.        step="{integer}"
        14.        index="{integer}"
        15.        scientific-display="{boolean}"
        16.        [display-units]="{boolean}"
        17.        [display-values]="{boolean}"
        18.        [display-stack-values]="{boolean}"
        19.        [multiplier]="{number}"
        20.        [color-thresholds]="{string}"
        21.        [subsets]="{string}"
        22.        [subseries]="{boolean}"
        23.        [refine-on-click-context]="{string}"
        24.        [refine-on-click[context]-context-field]="{string}">
        25. </ods-chart-serie>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
[chartType]| [string]()| Available types are: 'line', 'spline', 'arearange', 'areasplinerange', 'columnrange', 'area', 'areaspline', 'column', 'bar', 'pie', 'scatter'  
[functionY]| [string]()| Sets up the function that will be used to calculate aggregation value. 'COUNT' counts the number of documents for each category defined by expressionY.  
[expressionY]| [string]()| Sets up the facet used for aggregation  
[color]| [string]()| Defines the color used for this serie. see colors below  
[labelY]| [string]()| Specifies a custom label for the series  
labelsposition| [string]()| Specifies the position of labels. The authorized values are 'inside' or 'outside' (for pie charts only). _(default: 'outside')_  
innersize| [number]()| This parameter can be used to change a pie chart into a donut by creating a hole in the center. The value is expressed in pixels. _(default: 0)_  
[cumulative]| [boolean]()| Y values are accumulated  
logarithmic| [boolean]()| Displays the serie using a logarithmic scale _(default: false)_  
min| [integer]()| Minimum value to be displayed on the Y-axis. If not defined, it is computed automatically. _(default: null)_  
max| [integer]()| Maximum value to be displayed on the Y axis. If not defined, it is computed automatically. _(default: null)_  
step| [integer]()| Specifies the step between each tick on the Y-axis. If not defined, it is computed automatically. _(default: null)_  
index| [integer]()| Forces the display order of the serie. The higher is on top, the lower is below (starts from 1). _(default: null)_  
scientificDisplay| [boolean]()| When set to false, force the full display of the numbers on the Y-axis. _(default: true)_  
[displayUnits]| [boolean]()| Enables the display of the units defined for the field in the tooltip  
[displayValues]| [boolean]()| Enables the display of each invidual values in stacks  
[displayStackValues]| [boolean]()| Enables the display of the cumulated values on top of stacks  
[multiplier]| [number]()| Multiplies all values for this serie by the defined number  
[colorThresholds]| [string]()| An array of (value, color) objects. For each threshold value, if the Y value is above the threshold, the defined color is used. The format for this parameter is color-thresholds="[{'value': 5, 'color': '#00ff00'},{'value': 10, 'color': '#ffff00'}]"  
[subsets]| [string]()| Used when functionY is set to 'QUANTILES' to define the wanted quantile  
[subseries]| [boolean]()| An array of subseries. They are used for range, columnrange, and boxplot charts. Each item of the array contains an object like: {"func": "AVG", "yAxis": "myfield"}  
[refineOnClickContext]| [string]()| Context name or array of contexts name on which to refine when the series is clicked on. It won't work properly if the fieldX attribute of the parent odsChartQuery is a date or datetime field and if the associated timescale is not one of 'year', 'month', 'day', 'hour', 'minute'.  
[refineOnClick[context]ContextField]| [string]()| Name of the field that will be refined for each context


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| [chartType] | string | Available types are: 'line', 'spline', 'arearange', 'areasplinerange', 'columnrange', 'area', 'areaspline', 'column', 'bar', 'pie', 'scatter' |
| [functionY] | string | Sets up the function that will be used to calculate aggregation value. 'COUNT' counts the number of documents for each category defined by expressionY. |
| [expressionY] | string | Sets up the facet used for aggregation |
| [color] | string | Defines the color used for this serie. see colors below |
| [labelY] | string | Specifies a custom label for the series |
| labelsposition | string | Specifies the position of labels. The authorized values are 'inside' or 'outside' (for pie charts only).(default: 'outside') |
| innersize | number | This parameter can be used to change a pie chart into a donut by creating a hole in the center. The value is expressed in pixels.(default: 0) |
| [cumulative] | boolean | Y values are accumulated |
| logarithmic | boolean | Displays the serie using a logarithmic scale(default: false) |
| min | integer | Minimum value to be displayed on the Y-axis. If not defined, it is computed automatically.(default: null) |
| max | integer | Maximum value to be displayed on the Y axis. If not defined, it is computed automatically.(default: null) |
| step | integer | Specifies the step between each tick on the Y-axis. If not defined, it is computed automatically.(default: null) |
| index | integer | Forces the display order of the serie. The higher is on top, the lower is below (starts from 1).(default: null) |
| scientificDisplay | boolean | When set to false, force the full display of the numbers on the Y-axis.(default: true) |
| [displayUnits] | boolean | Enables the display of the units defined for the field in the tooltip |
| [displayValues] | boolean | Enables the display of each invidual values in stacks |
| [displayStackValues] | boolean | Enables the display of the cumulated values on top of stacks |
| [multiplier] | number | Multiplies all values for this serie by the defined number |
| [colorThresholds] | string | An array of (value, color) objects. For each threshold value, if the Y value is above the threshold, the defined color is used. The format for this parameter is color-thresholds="[{'value': 5, 'color': '#00ff00'},{'value': 10, 'color': '#ffff00'}]" |
| [subsets] | string | Used when functionY is set to 'QUANTILES' to define the wanted quantile |
| [subseries] | boolean | An array of subseries. They are used for range, columnrange, and boxplot charts. Each item of the array contains an object like: {"func": "AVG", "yAxis": "myfield"} |
| [refineOnClickContext] | string | Context name or array of contexts name on which to refine when the series is clicked on. It won't work properly if the fieldX attribute of the parent odsChartQuery is a date or datetime field and if the associated timescale is not one of 'year', 'month', 'day', 'hour', 'minute'. |
| [refineOnClick[context]ContextField] | string | Name of the field that will be refined for each context |

---
### odsClearAllFilters

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsClearAllFilters widget displays a button that will clear all active filters in the given context.


#### Usage

as element:
      
      1. <ods-clear-all-filters
        2.        context="{CatalogContext|DatasetContext|CatalogContext[]|DatasetContext[]}"
        3.        except="{String[]}">
        4. </ods-clear-all-filters>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
context| [CatalogContext]()[DatasetContext]()[CatalogContext[]]()[DatasetContext[]]()| Catalog Context or Dataset Context to display the filters of, or a list of contexts  
except| [String[]]()| An array of parameters to exclude from the clearing operation


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| context | CatalogContextDatasetContextCatalogContext[]DatasetContext[] | Catalog ContextorDataset Contextto display the filters of, or a list of  contexts |
| except | String[] | An array of parameters to exclude from the clearing operation |

---
### odsColorGradient

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsColorGradient widget exposes the results of an analysis transposed to a set of colors for each X value. The results are available in the scope.

This widget can be used directly on the odsMap's `color-categories` parameter with the `display=categories` mode. It can also be used on the AngularJS ngRepeat directive to build custom scales.


#### Usage

as attribute
      
      1. <ANY ods-color-gradient="{string}"
        2.      ods-color-gradient-context="{DatasetContext}"
        3.      ods-color-gradient-x="{string}"
        4.      ods-color-gradient-serie="{string}"
        5.      ods-color-gradient-high="{string}"
        6.      ods-color-gradient-low="{string}"
        7.      ods-color-gradient-nb-classes="{integer}"
        8.      ods-color-gradient-pow-exponent="{integer}">
        9.    ...
        10. </ANY>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
odsColorGradient| [string]()| Variable name to use to output the color gradient data structure. variable['colors'] can be used in ods-maps. 'values', 'range' keys are also available.  
odsColorGradientContext| [DatasetContext]()| Dataset Context to use  
odsColorGradientX| [string]()| The X-axis of the analysis  
odsColorGradientSerie| [string]()| FUNC(expression) where FUNC is AVG, SUM, MIN, MAX, etc... and expression is the field id to work on.  
odsColorGradientHigh| [string]()| RGB or HEX color code for highest value of the analysis serie. ex: "rgb(255, 0, 0)", "#abc" _(default: 'rgb(0, 55, 237)')_  
odsColorGradientLow| [string]()| RGB or HEX color code for the lowest value of the analysis serie. ex: "rgb(125, 125, 125)", "#ff009a" _(default: 'rgb(180, 197, 241)')_  
odsColorGradientNbClasses| [integer]()| Number of classes, ie number of color to compute. Mandatory to get a consistent legend with the corresponding number of grades/classes. _(default: undefined)_  
odsColorGradientPowExponent| [integer]()| Set to `1` for a linear scale (default value), to `0.3` to approximate a logarithmic scale. Power scale tends to look like a log scale when the exponent is less than `1` and tends to an exponential scale when bigger than `1`. _(default: undefined)_


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| odsColorGradient | string | Variable name to use to output the color gradient data structure. variable['colors'] can be used in ods-maps. 'values', 'range' keys are also available. |
| odsColorGradientContext | DatasetContext | Dataset Contextto use |
| odsColorGradientX | string | The X-axis of the analysis |
| odsColorGradientSerie | string | FUNC(expression) where FUNC is AVG, SUM, MIN, MAX, etc... and expression is the field id to work on. |
| odsColorGradientHigh | string | RGB or HEX color code for highest value of the analysis serie. ex: "rgb(255, 0, 0)", "#abc"(default: 'rgb(0, 55, 237)') |
| odsColorGradientLow | string | RGB or HEX color code for the lowest value of the analysis serie. ex: "rgb(125, 125, 125)", "#ff009a"(default: 'rgb(180, 197, 241)') |
| odsColorGradientNbClasses | integer | Number of classes, ie number of color to compute. Mandatory to get a consistent legend with the corresponding number of grades/classes.(default: undefined) |
| odsColorGradientPowExponent | integer | Set to1for a linear scale (default value), to0.3to approximate a logarithmic scale. Power scale tends to look like a log scale when the exponent is less than1and tends to an exponential scale when bigger than1.(default: undefined) |

---
### odsCrossTable

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsCrossTable widget creates a cross table from a context. It supports multiple aggregations for a single column field and multiple row fields.


#### Usage

as element:
      
      1. <ods-cross-table
        2.        context="{DatasetContext}"
        3.        rows="{string}"
        4.        column="{string}"
        5.        serie-xxx-label="{string}"
        6.        serie-xxx-func="{string}"
        7.        serie-xxx-expr="{string}"
        8.        repeat-row-headers="{boolean}"
        9.        display-intermediary-results="{boolean}"
        10.        number-precision="{integer}">
        11. </ods-cross-table>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
context| [DatasetContext]()| Dataset Context from which data is extracted  
rows| [string]()| A comma-separated list of field names which will be used for row headers' values. These fields must all be facets.  
column| [string]()| Name of the field which will be used for column header's values. This field must be a facet.  
serieXxxLabel| [string]()| Label of the series, which will be displayed as column header (Xxx being the name of the series).  
serieXxxFunc| [string]()| Function (SUM, AVG, COUNT, etc.) used to aggregate the series analysis (Xxx being the name of the series)  
serieXxxExpr| [string]()| Name of the field used for the series analysis (Xxx being the name of the series)  
repeatRowHeaders| [boolean]()| Controls whether to repeat the row headers on each line or not. _(default: false)_  
displayIntermediaryResults| [boolean]()| Controls whether to display intermediary subtotals, subaverages, etc. _(default: false)_  
numberPrecision| [integer]()| The number of decimals to display for numeric values _(default: 3)_


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| context | DatasetContext | Dataset Contextfrom which data is extracted |
| rows | string | A comma-separated list of field names which will be used for row headers' values. These fields must all be facets. |
| column | string | Name of the field which will be used for column header's values. This field must be a facet. |
| serieXxxLabel | string | Label of the series, which will be displayed as column header (Xxx being the name of the series). |
| serieXxxFunc | string | Function (SUM, AVG, COUNT, etc.) used to aggregate the series analysis (Xxx being the name of the series) |
| serieXxxExpr | string | Name of the field used for the series analysis (Xxx being the name of the series) |
| repeatRowHeaders | boolean | Controls whether to repeat the row headers on each line or not.(default: false) |
| displayIntermediaryResults | boolean | Controls whether to display intermediary subtotals, subaverages, etc.(default: false) |
| numberPrecision | integer | The number of decimals to display for numeric values(default: 3) |

---
### odsDatasetContext

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsDatasetContext widget represents a dataset from a chosen domain and a set of parameters used to query its data. One or more widgets can use odsDatasetContext: it allows them to share information (i.e., the query parameters).

For example, a widget that displays a filter (odsFacets) can be plugged into the same context as a table view widget (odsTable) so that the user can filter the data displayed in the table.

odsDatasetContext creates a new child scope, within which its declared contexts are available for any other widget used inside that odsDatasetContext element. odsDatasetContext widgets can also be nested inside each other.

A single odsDatasetContext can declare one or several contexts, which are initialized when declared through the **context** parameter. Each context is configured using parameters prefixed by the context name (`contextname-setting`, e.g., mycontext-domain).

**Properties of odsDatasetContext used as variable**

Once created, the context is accessible as a variable named after it. The context contains properties that can be accessed directly:

  * `domainUrl`: full URL of the domain of the context that can be used to create links
  * `parameters`: parameters object of the context
  * `dataset`: dataset object for the context
  * `getDownloadURL(format[, dict options])`: method that returns a URL to download the data, including currently active filters (e.g. refinements, queries etc.). By default the URL will allow downloading a CSV export, but another format can be passed, such as "geojson" or "json". Two optional parameters are also available: `{'use_labels_for_header': '<true/false>', 'fields': '<list of comma separated field name>'}`
  * `getQueryStringURL([dict options])`: method that builds the URL suffix (`?key1=value1&key2=value2&...`) based on context parameters (active filters, refinement, sort, query, etc.). The optional dictionary parameter allows building the URL with additional key/value parameters.
  * `getV2DownloadURL(format[, dict options])`: method that returns an Explore API V2.1 URL to download the data, including currently active filters. It can be used to export Explore API V2.1 specific formats such as "xlsx". An optional parameter is available: `{'fields': '<list of comma separated field name>'}`
  * `getV2QueryStringURL([dict options])`: method that builds the URL suffix (`?key1=value1&key2=value2&...`) based on context parameters, intended for an Explore API V2.1 URL. The optional dictionary parameter allows building the URL with additional key/value parameters.




#### Usage

as element:
      
      1. <ods-dataset-context
        2.        context="{string}"
        3.        dataset="{string}"
        4.        domain="{string}"
        5.        apikey="{string}"
        6.        sort="{string}"
        7.        parameters="{object}"
        8.        refresh-delay="{number}"
        9.        parameters-from-context="{string}"
        10.        url-sync="{boolean}">
        11. </ods-dataset-context>
    
    

as attribute
      
      1. <ANY ods-dataset-context
        2.      context="{string}"
        3.      dataset="{string}"
        4.      domain="{string}"
        5.      apikey="{string}"
        6.      sort="{string}"
        7.      parameters="{object}"
        8.      refresh-delay="{number}"
        9.      parameters-from-context="{string}"
        10.      url-sync="{boolean}">
        11.    ...
        12. </ANY>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
context| [string]()|  _(mandatory)_ Name, or list of names separated by commas, of context(s) to declare. Context names must be in lowercase, can only contain alphanumerical characters, and cannot begin with a number, "data", or "x".  
dataset| [string]()|  _(mandatory)_ Identifier of the dataset(s) on which the context is based.  
domain| [string]()| Domain where the dataset(s) can be found. Since the domain value is used to construct a URL to an API root, it can be:

  * an alphanumeric string (e.g., _mydomain_): it will assume that it is a Huwise domain (e.g., _mydomain.huwise.com_)
  * a hostname (e.g., _data.mydomain.com_)
  * a relative path (e.g., _/monitoring_): it will be relative to the hostname of the current page
  * a hostname and a path (e.g., _data.mydomain.com/monitoring_)

By default, if the domain parameter is not set, ODSWidgetsConfig.defaultDomain is used. _(default: ODSWidgetsConfig.defaultDomain)_  
apikey| [string]()| API key to use in every API call for the context (see [Generating an API key](https://userguide.huwise.com/en/articles/2044226)). _(default: none)_  
sort| [string]()| Sorts expression to apply by default to all widgets plugged to the declared context. The expression should be written using one of the following syntaxes:

  * `field` for an ascending order,
  * `-field` for a descending order.

_(default: none)_  
parameters| [object]()| Object holding parameters to apply to the context when it is created. Any parameter from the API can be used here (such as `q` or `refine.FIELD`). _(default: none)_  
refreshDelay| [number]()| Number of milliseconds to wait before the context is automatically refreshed. If this parameter is not set, the context will not automatically refresh. The minimum delay is 10000ms. _(default: none)_  
parametersFromContext| [string]()| Name of another declared context to replicate the parameters and queries from. Any modification on the parameters of this context or the original one will be applied to both. _(default: none)_  
urlSync| [boolean]()| Enables the synchronization of the parameters to the page's parameters (query string). When sharing the page with parameters in the URL, the context will use them; and if the context parameters change, the URL parameters will change. Note: if this parameter is enabled, `parameters` and `parametersFromContext` won't have any effect. There can only be a single context with URL synchronization enabled. Else the behavior will be unpredictable. _(default: none)_


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| context | string | (mandatory)Name, or list of names separated by commas, of context(s) to declare. Context names must be in lowercase, can only contain alphanumerical characters, and cannot begin with a number, "data", or "x". |
| dataset | string | (mandatory)Identifier of the dataset(s) on which the context is based. |
| domain | string | Domain where the dataset(s) can be found. Since the domain value is used to construct a URL to an API root, it can be:an alphanumeric string (e.g.,mydomain): it will assume that it is a Huwise domain (e.g.,mydomain.huwise.com)a hostname (e.g.,data.mydomain.com)a relative path (e.g.,/monitoring): it will be relative to the hostname of the current pagea hostname and a path (e.g.,data.mydomain.com/monitoring)By default, if the domain parameter is not set,ODSWidgetsConfig.defaultDomainis used.(default: ODSWidgetsConfig.defaultDomain) |
| apikey | string | API key to use in every API call for the context (seeGenerating an API key).(default: none) |
| sort | string | Sorts expression to apply by default to all widgets plugged to the declared context. The expression should be written using one of the following syntaxes:fieldfor an ascending order,-fieldfor a descending order.(default: none) |
| parameters | object | Object holding parameters to apply to the context when it is created. Any parameter from the API can be used here (such asqorrefine.FIELD).(default: none) |
| refreshDelay | number | Number of milliseconds to wait before the context is automatically refreshed. If this parameter is not set, the context will not automatically refresh. The minimum delay is 10000ms.(default: none) |
| parametersFromContext | string | Name of another declared context to replicate the parameters and queries from. Any modification on the parameters of this context or the original one will be applied to both.(default: none) |
| urlSync | boolean | Enables the synchronization of the parameters to the page's parameters (query string). When sharing the page with parameters in the URL, the context will use them; and if the context parameters change, the URL parameters will change.Note: if this parameter is enabled,parametersandparametersFromContextwon't have any effect. There can only be a single context with URL synchronization enabled. Else the behavior will be unpredictable.(default: none) |

---
### odsDatasetSchema

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsDatasetSchema widget displays a table describing the schema of a dataset. For each field, it provides the label, name, description, type, and an example.


#### Usage

as element:
      
      1. <ods-dataset-schema
        2.        context="{DatasetContext}">
        3. </ods-dataset-schema>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
context| [DatasetContext]()| Dataset Context


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| context | DatasetContext | Dataset Context |

---
### odsDateRangeSlider

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsDateRangeSlider widget displays a range slider to select the two bounds of a date range.


#### Usage

as element:
      
      1. <ods-date-range-slider
        2.        context="{DatasetContext|DatasetContext[]}"
        3.        initial-from="{string}"
        4.        initial-to="{string}"
        5.        start-bound="{expression}"
        6.        end-bound="{expression}"
        7.        date-format="{string}"
        8.        date-field="{string}"
        9.        precision="{string}"
        10.        suffix="{string}"
        11.        to="{string}"
        12.        from="{string}">
        13. </ods-date-range-slider>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
context| [DatasetContext]()[DatasetContext[]]()| Dataset Context or array of context to use  
initialFrom| [string]()| Default date for the "from" field: "yesterday", "now", or a string representing a date _(default: none)_  
initialTo| [string]()| Default date for the "to" field: "yesterday", "now", or a string representing a date _(default: none)_  
startBound| [expression]()| Beginning bound of the range slider, it will define the minimum selectable from "yesterday", "now", or a string representing a date. As an AngularJS expression is expected, no need to use syntax for variables or expressions, and if you want to provide a static string value, surround it with simple quotes. _(default: none)_  
endBound| [expression]()| End bound of the range slider, it will define the maximum selectable to "yesterday", "now", or a string representing a date. As an AngularJS expression is expected, no need to use syntax for variables or expressions, and if you want to provide a static string value, surround it with simple quotes. _(default: none)_  
dateFormat| [string]()| Defines the format to render the two bounds and the selection. _(default: 'YYYY-MM-DD')_  
dateField| [string]()| Date field to query on. If no field is provided, the first date type field of the dataset is used. _(default: none)_  
precision| [string]()| Defines the precision, 'day', 'month' or 'year', default is 'day' _(default: 'day')_  
suffix| [string]()| Context parameter query suffix. Used to avoid collision with other widget queries. _(default: none)_  
to| [string]()| Sets a variable that will get the iso formatted value of the first input _(default: none)_  
from| [string]()| Sets a variable that will get the iso formatted value of the second input _(default: none)_


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| context | DatasetContextDatasetContext[] | Dataset Contextor array of context to use |
| initialFrom | string | Default date for the "from" field: "yesterday", "now", or a string representing a date(default: none) |
| initialTo | string | Default date for the "to" field: "yesterday", "now", or a string representing a date(default: none) |
| startBound | expression | Beginning bound of the range slider, it will define the minimum selectable from "yesterday", "now", or a string representing a date. As an AngularJS expression is expected, no need to use  syntax for variables or expressions, and if you want to provide a static string value, surround it with simple quotes.(default: none) |
| endBound | expression | End bound of the range slider, it will define the maximum selectable to "yesterday", "now", or a string representing a date. As an AngularJS expression is expected, no need to use  syntax for variables or expressions, and if you want to provide a static string value, surround it with simple quotes.(default: none) |
| dateFormat | string | Defines the format to render the two bounds and the selection.(default: 'YYYY-MM-DD') |
| dateField | string | Date field to query on. If no field is provided, the first date type field of the dataset is used.(default: none) |
| precision | string | Defines the precision, 'day', 'month' or 'year', default is 'day'(default: 'day') |
| suffix | string | Context parameter query suffix. Used to avoid collision with other widget queries.(default: none) |
| to | string | Sets a variable that will get the iso formatted value of the first input(default: none) |
| from | string | Sets a variable that will get the iso formatted value of the second input(default: none) |

---
### odsDatetime

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsDatetime widget gets the ISO local datetime and stores it into a variable (into the scope).

It is an equivalent to moment().format() javascript call. The current scope gains a refreshDatetime method that will refresh the variable with the current datetime.


#### Usage

as attribute
      
      1. <ANY ods-datetime>
        2.    ...
        3. </ANY>
    
    

### Directive info

  * This directive creates new scope.




---
### odsDisqus

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsDisqus widget shows a Disqus panel where users can comment on the page.


#### Usage

as element:
      
      1. <ods-disqus
        2.        shortname="{string}"
        3.        identifier="{string}">
        4. </ods-disqus>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
shortname| [string]()| Disqus short name for your account. If not specified, ODSWidgetsConfig.disqusShortname will be used.  
identifier| [string]()| By default, the discussion is tied to the URL of the page. If you want to be independent from the URL or share the discussion between two or more pages, you can define an identifier in this parameter. Disqus recommends always doing this from the start. _(default: none)_


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| shortname | string | Disqus short name for your account. If not specified,ODSWidgetsConfig.disqusShortnamewill be used. |
| identifier | string | By default, the discussion is tied to the URL of the page. If you want to be independent from the URL or share the discussion between two or more pages, you can define an identifier in this parameter. Disqus recommends always doing this from the start.(default: none) |

---
### odsDomainStatistics

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsDomainStatistics widget enumerates statistic values for a given catalog and injects them as variables in the context.

The following AngularJS variables are available:

  * `CONTEXTNAME.stats.dataset`: the number of datasets
  * `CONTEXTNAME.stats.keyword`: the number of keywords
  * `CONTEXTNAME.stats.publisher`: the number of publishers
  * `CONTEXTNAME.stats.theme`: the number of themes



### First syntax: when declaring a catalog context, directly inject these values
      
      1. <ods-catalog-context context="catalog" catalog-domain="dataset" ods-domain-statistics>
        2.     {{ catalog.stats.dataset }} datasets
        3. </ods-catalog-context>
    
    

### Second syntax : inject them using a dedicated tag
      
      1. <ods-domain-statistics context="catalog">
        2.     {{ catalog.stats.dataset }} datasets
        3. </ods-domain-statistics>
    
    


#### Usage

as element:
      
      1. <ods-domain-statistics
        2.        context="{DatasetContext}">
        3. </ods-domain-statistics>
    
    

as attribute
      
      1. <ANY ods-domain-statistics
        2.      context="{DatasetContext}">
        3.    ...
        4. </ANY>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
context| [DatasetContext]()| Catalog Context to use


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| context | DatasetContext | Catalog Contextto use |

---
### odsFacetResults

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsFacetResults widget fetches the results of enumerating the values ("categories") of a facet and exposes it in a variable available in the scope. You can use this widget with the AngularJS ngRepeat directive to build a list of results.

The variable is an array of objects, each containing the following properties:

  * `name`: the label of the category
  * `path`: the path to use to refine on this category
  * `state`: "displayed" or "refined"
  * `count`: the number of records in this category




#### Usage

as attribute
      
      1. <ANY ods-facet-results="{string}"
        2.      ods-facet-results-context="{CatalogContext|DatasetContext}"
        3.      ods-facet-results-facet-name="{string}"
        4.      ods-facet-results-sort="{string}">
        5.    ...
        6. </ANY>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
odsFacetResults| [string]()| Variable name to use _(default: results)_  
odsFacetResultsContext| [CatalogContext]()[DatasetContext]()| Catalog Context or Dataset Context to use  
odsFacetResultsFacetName| [string]()| Name of the facet to enumerate  
odsFacetResultsSort| [string]()| Sorting method used on categories:

  * `count` or `-count` to sort by number of items in each category
  * `num` or `-num` to sort by the name of category, if it is a number
  * `alphanum` or `-alphanum` to sort by the name of the category

Note: the `-` character before the name of the sorting method indicates that values will be sorted in descending order instead of ascending order. _(default: count)_


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| odsFacetResults | string | Variable name to use(default: results) |
| odsFacetResultsContext | CatalogContextDatasetContext | Catalog ContextorDataset Contextto use |
| odsFacetResultsFacetName | string | Name of the facet to enumerate |
| odsFacetResultsSort | string | Sorting method used on categories:countor-countto sort by number of items in each categorynumor-numto sort by the name of category, if it is a numberalphanumor-alphanumto sort by the name of the categoryNote: the-character before the name of the sorting method indicates that values will be sorted in descending order instead of ascending order.(default: count) |

---
### odsFacets

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsFacets widget displays filters based on a dataset or a domain's catalog of datasets. This widget allows to dynamically refine on one or more categories for the defined context (i.e., each filter being composed of several categories, which are values of the field the filter is based on).

For example, odsFacet can be used to refine the data displayed in a table (odsTable) to see only the desired data.

Suppose the widget is used without any configuration. In that case, it will display by default filters from all the "facet" fields of a dataset when used with a Dataset Context. It will display by default filters from typical metadata from a dataset catalog when used with a Catalog Context.
      
      1. <ods-facets context="mycontext"></ods-facets>
    
    

**odsFacet**

The odsFacet widget is a widget that can only be used based on odsFacets. It is used to configure which facets should be displayed by odsFacets, since odsFacets used alone does not allow to display only specific facets among all the default ones of the dataset. odsFacet supports the following parameters:

  * name
  * sort
  * visibleItems
  * hideIfSingleCategory
  * hideCategoryIf



Note: these parameters are the same as some used for odsFacets. For more information about configuration, see the odsFacets parameters table.

odsFacet allows to configure which facets are displayed using the **name** parameter.
      
      1. <ods-facets context="mycontext">
        2.     <h3>First field</h3>
        3.     <ods-facet name="myfield"></ods-facet>
        4.  
        5.     <h3>Second field</h3>
        6.     <ods-facet name="mysecondfield"></ods-facet>
        7. </ods-facets>
    
    

Regular HTML is supported within the odsFacet tag to change the display template of each category. The available variables within the template are:

  * `facetName`: name of the field that the filter is based on
  * `category.name`: value of the category
  * `category.path`: complete path to the category, including hierarchical levels
  * `category.state`: refined, excluded, or displayed



An `ng-non-bindable` wrapper element must be used around the display template for it to work properly. Note: There must not be any space character between the odsFacet tag and the span element, as it may prevent the widget from working properly.
      
      1. <ods-facets context="mycontext">
        2.     <ods-facet name="myfield"><span ng-non-bindable>
        3.         {{category.name}} @ {{category.state}}
        4.     </span></ods-facet>
        5. </ods-facets>
    
    


#### Usage

as element:
      
      1. <ods-facets
        2.        context="{DatasetContext}"
        3.        name="{string}"
        4.        title="{string}"
        5.        sort="{string}"
        6.        visible-items="{number}"
        7.        hide-if-single-category="{boolean}"
        8.        hide-category-if="{string}"
        9.        disjunctive="{boolean}"
        10.        timerange-filter="{boolean}"
        11.        context="{string}"
        12.        value-search="{string}"
        13.        refine-also="{DatasetContext|CatalogContext|DatasetContext[]|CatalogContext[]}"
        14.        [context-name]-facet-name="{string}">
        15. </ods-facets>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
context| [DatasetContext]()|  _(mandatory)_ Catalog Context or Dataset Context to use  
name| [string]()|  _(mandatory)_ Name of the field the filter is based on  
title| [string]()| Title to display above the filter _(default: none)_  
sort| [string]()| Sorting method used on categories:

  * `count` or `-count` to sort by number of items in each category
  * `num` or `-num` to sort by the name of category, if it is a number
  * `alphanum` or `-alphanum` to sort by the name of the category Note: the `-` character before the name of the sorting method indicates that values will be sorted in descending order instead of ascending order. Configuring a specific order is also possible, by setting a list of value: `['value1', 'value2']`.

_(default: -count)_  
visibleItems| [number]()| Number of categories to show. If there are more categories for the filter, they are collapsed by default, but can be expanded by clicking on a "more" link. _(default: 6)_  
hideIfSingleCategory| [boolean]()| When set to `true`, hides filters if only one category to refine on is available. _(default: false)_  
hideCategoryIf| [string]()| AngularJS expression to evaluate: if it evaluates to `true`, the category is displayed. In the expression, the following elements can be used:

  * `category.name` (value of the category)
  * `category.path` (complete path to the category, including hierarchical levels)
  * `category.state` (refined, excluded, or displayed)

_(default: none)_  
disjunctive| [boolean]()| When set to `true`, the filter is in disjunctive mode, which means that other available values can also be selected after a first value is selected. All selected values are combined as "or". For example, after clicking "red", "green" and "blue" can also be clicked. The resulting values can be green, red, or blue. Note: this parameter is directly related to the schema of the dataset. For this parameter to work properly, the field must allow multiple selections in filters. For more information, see [Defining a dataset schema](https://userguide.huwise.com/en/articles/2044866)). _(default: false)_  
timerangeFilter| [boolean]()| When set to `true`, an option to filter using a time range is displayed above the categories. This parameter only works for date and datetime fields and must be used with a context (see **context** parameter). _(default: false)_  
context| [string]()| Name of the context to refine on. This parameter is mandatory for the **timerangeFilter** parameter. _(default: none)_  
valueSearch| [string]()| When set to `true`, a search box is displayed above the categories to search within the available categories. If `suggest`, the matching categories are not displayed until there is at least one character typed into the search box, effectively making it into a suggest-like search box. _(default: none)_  
refineAlso| [DatasetContext]()[CatalogContext]()[DatasetContext[]]()[CatalogContext[]]()| Enables the widget to apply its refinements on other contexts, e.g., for contexts which share a common data. The value of this parameter should be the name of another context or a list of contexts. _(default: none)_  
[contextName]FacetName| [string]()| Name of the facet in one of the other contexts, defined through the **refineAlso** parameter, that the original facet should be mapped on. `[contextName]` must be replaced with the name of that other context. _(default: Current facet's name)_


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| context | DatasetContext | (mandatory)Catalog ContextorDataset Contextto use |
| name | string | (mandatory)Name of the field the filter is based on |
| title | string | Title to display above the filter(default: none) |
| sort | string | Sorting method used on categories:countor-countto sort by number of items in each categorynumor-numto sort by the name of category, if it is a numberalphanumor-alphanumto sort by the name of the categoryNote: the-character before the name of the sorting method indicates that values will be sorted in descending order instead of ascending order.Configuring a specific order is also possible, by setting a list of value:['value1', 'value2'].(default: -count) |
| visibleItems | number | Number of categories to show. If there are more categories for the filter, they are collapsed by default, but can be expanded by clicking on a "more" link.(default: 6) |
| hideIfSingleCategory | boolean | When set totrue, hides filters if only one category to refine on is available.(default: false) |
| hideCategoryIf | string | AngularJS expression to evaluate: if it evaluates totrue, the category is displayed. In the expression, the following elements can be used:category.name(value of the category)category.path(complete path to the category, including hierarchical levels)category.state(refined, excluded, or displayed)(default: none) |
| disjunctive | boolean | When set totrue, the filter is in disjunctive mode, which means that other available values can also be selected after a first value is selected. All selected values are combined as "or". For example, after clicking "red", "green" and "blue" can also be clicked. The resulting values can be green, red, or blue.Note: this parameter is directly related to the schema of the dataset. For this parameter to work properly, the field must allow multiple selections in filters. For more information, seeDefining a dataset schema).(default: false) |
| timerangeFilter | boolean | When set totrue, an option to filter using a time range is displayed above the categories. This parameter only works for date and datetime fields and must be used with a context (seecontextparameter).(default: false) |
| context | string | Name of the context to refine on. This parameter is mandatory for thetimerangeFilterparameter.(default: none) |
| valueSearch | string | When set totrue, a search box is displayed above the categories to search within the available categories. Ifsuggest, the matching categories are not displayed until there is at least one character typed into the search box, effectively making it into a suggest-like search box.(default: none) |
| refineAlso | DatasetContextCatalogContextDatasetContext[]CatalogContext[] | Enables the widget to apply its refinements on other contexts, e.g., for contexts which share a common data. The value of this parameter should be the name of another context or a list of contexts.(default: none) |
| [contextName]FacetName | string | Name of the facet in one of the other contexts, defined through therefineAlsoparameter, that the original facet should be mapped on.[contextName]must be replaced with the name of that other context.(default: Current facet's name) |

---
### odsFilterSummary

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsFilterSummary widget displays a summary of all the active filters in a context: text search, refinements, etc.


#### Usage

as element:
      
      1. <ods-filter-summary
        2.        context="{CatalogContext|DatasetContext|CatalogContext[]|DatasetContext[]}"
        3.        exclude="{string}"
        4.        clear-all-button="{boolean}"
        5.        hide-contexts-labels="{boolean}"
        6.        [mycontext-label]="{string}">
        7. </ods-filter-summary>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
context| [CatalogContext]()[DatasetContext]()[CatalogContext[]]()[DatasetContext[]]()| Catalog Context or Dataset Context to display the filters of. Can also be a list of contexts.  
exclude| [string]()| Optional: Name of parameters not to display, separated by commas. For example, `q,rows,start` _(default: none)_  
clearAllButton| [boolean]()| Optional: display a "clear all" button underneath the active filters' list. _(default: true)_  
hideContextsLabels| [boolean]()| Optional: if you are working with multiple contexts, the context's label will be displayed within the filter. Set this option to true if you'd like not to display those. _(default: false)_  
[mycontextLabel]| [string]()| Optional: if you are working with multiple contexts, the context's name (that is "mycontext") will be displayed within the filter. Use this option to specify a custom label.


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| context | CatalogContextDatasetContextCatalogContext[]DatasetContext[] | Catalog ContextorDataset Contextto display the filters of. Can also be a list of contexts. |
| exclude | string | Optional: Name of parameters not to display, separated by commas. For example,q,rows,start(default: none) |
| clearAllButton | boolean | Optional: display a "clear all" button underneath the active filters' list.(default: true) |
| hideContextsLabels | boolean | Optional: if you are working with multiple contexts, the context's label will be displayed within the filter. Set this option to true if you'd like not to display those.(default: false) |
| [mycontextLabel] | string | Optional: if you are working with multiple contexts, the context's name (that is "mycontext") will be displayed within the filter. Use this option to specify a custom label. |

---
### odsGauge

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsGauge widget displays a gauge in one of the two following modes: circle or horizontal bar. The widget relies on CSS3 and SVG. As a result, it is entirely customizable in CSS.

The widget will decide its size based on its width, so you can make it larger or smaller using the CSS `width` property; however, the widget will always take the necessary height, so forcing the height using CSS won't work. Values exceeding the given max will be represented as a full gauge, whereas values lower than 0 will be represented as an empty gauge.


#### Usage

as element:
      
      1. <ods-gauge
        2.        display-mode="{string}"
        3.        max="{float}"
        4.        value="{float}">
        5. </ods-gauge>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
displayMode| [string]()| Type of chart: 'circle' or 'bar' _(default: circle)_  
max| [float]()| The maximum value for the gauge _(default: 100)_  
value| [float]()| A number between 0 and the defined `max` value


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| displayMode | string | Type of chart: 'circle' or 'bar'(default: circle) |
| max | float | The maximum value for the gauge(default: 100) |
| value | float | A number between 0 and the definedmaxvalue |

---
### odsGeoNavigation

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsGeoNavigation widget allows to visually navigate a catalog using geographic metadata (currently, only the "Geographic coverage" metadata). The navigation is similar to `odsFacets`, but with a visual indication (map) of the current location used as a filter.


#### Usage

as element:
      
      1. <ods-geo-navigation
        2.        context="{CatalogContext}"
        3.        min-level="{number}"
        4.        max-level="{number}"
        5.        default-filter="{string}"
        6.        ascending-filter="{boolean}">
        7. </ods-geo-navigation>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
context| [CatalogContext]()| Catalog context to use.  
minLevel| [number]()| Highest level available for navigation (countries are 10, other levels depend on the country)  
maxLevel| [number]()| Lowest level available for navigation (countries are 10, other levels depend on the country). If not set, the user will be able to navigate to the lowest available level. _(default: none)_  
defaultFilter| [string]()| Path of Geographic References leading to the filter's starting point (e.g. `world/world_fr/fr_40_52`).  
ascendingFilter| [boolean]()| When set to `true`, the "Display all datasets that include current selection" (ascending filter) option will be active by default. _(default: false)_


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| context | CatalogContext | Catalog contextto use. |
| minLevel | number | Highest level available for navigation (countries are 10, other levels depend on the country) |
| maxLevel | number | Lowest level available for navigation (countries are 10, other levels depend on the country). If not set, the user will be able to navigate to the lowest available level.(default: none) |
| defaultFilter | string | Path of Geographic References leading to the filter's starting point (e.g.world/world_fr/fr_40_52). |
| ascendingFilter | boolean | When set totrue, the "Display all datasets that include current selection" (ascending filter) option will be active by default.(default: false) |

---
### odsGeotooltip

**Module:** `ods-widgets`
**Type:** Directive

#### Description

When used to surround a text, the odsGeotooltip widget displays a tooltip showing a point and/or a shape in a map.


#### Usage

as element:
      
      1. <ods-geotooltip
        2.        coords="{Array|string}"
        3.        geojson="{Object}"
        4.        record="{Object}"
        5.        width="{number}"
        6.        height="{number}"
        7.        delay="{number}">
        8. </ods-geotooltip>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
coords| [Array]()[string]()| Coordinates of a point to display in the tooltip; either an array of two numbers as [latitude, longitude], or a string under the form of "latitude,longitude". If you use a string, surround it with simple quotes to ensure Angular treats it as a string. If you are working with a record (e.g., using odsResultEnumerator), you can directly use the content of a `geo_point_2d` field. _(default: none)_  
geojson| [Object]()| GeoJSON object of a shape to display in the tooltip. If you are working with a record (e.g., using odsResultEnumerator), you can directly use the content of a `geo_shape` field. _(default: none)_  
record| [Object]()| A record object (e.g., from odsResultEnumerator) from which the geometry will be taken (this is the `geometry` property of the record) _(default: none)_  
width| [number]()| Width of the tooltip, in pixels _(default: 200)_  
height| [number]()| Height of the tooltip, in pixels _(default: 200)_  
delay| [number]()| Delay before the tooltip appears on hover, in milliseconds _(default: 500)_


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| coords | Arraystring | Coordinates of a point to display in the tooltip; either an array of two numbers as [latitude, longitude], or a string under the form of "latitude,longitude". If you use a string, surround it with simple quotes to ensure Angular treats it as a string. If you are working with a record (e.g., usingodsResultEnumerator), you can directly use the content of ageo_point_2dfield.(default: none) |
| geojson | Object | GeoJSON object of a shape to display in the tooltip. If you are working with a record (e.g., usingodsResultEnumerator), you can directly use the content of ageo_shapefield.(default: none) |
| record | Object | A record object (e.g., fromodsResultEnumerator) from which the geometry will be taken (this is thegeometryproperty of the record)(default: none) |
| width | number | Width of the tooltip, in pixels(default: 200) |
| height | number | Height of the tooltip, in pixels(default: 200) |
| delay | number | Delay before the tooltip appears on hover, in milliseconds(default: 500) |

---
### odsGetElementLayout

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsGetElementLayout widget gets the height and width of an element. The variable is an object that contains 2 keys: 'height' and 'width'.


#### Usage

as attribute
      
      1. <ANY ods-get-element-layout>
        2.    ...
        3. </ANY>
    
    

### Directive info

  * This directive creates new scope.




---
### odsGetWindowLayout

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsGetElementLayout widget gets the height and width of the window. The variable is an object that contains 2 keys: 'height' and 'width'.


#### Usage

as attribute
      
      1. <ANY ods-get-window-layout>
        2.    ...
        3. </ANY>
    
    

### Directive info

  * This directive creates new scope.




---
### odsGist

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsGist widget integrates a GitHub Gist widget with a "copy to clipboard" button into a page.


#### Usage

as element:
      
      1. <ods-gist
        2.        username="{string}"
        3.        gist-id="{string}">
        4. </ods-gist>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
username| [string]()| The GitHub username  
gist-id| [string]()| The Gist identifier. See the Gist URL to find it.


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| username | string | The GitHub username |
| gist-id | string | The Gist identifier. See the Gist URL to find it. |

---
### odsHubspotForm

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsHubspotForm widget integrates a HubSpot form given a portal ID and the form ID.


#### Usage

as element:
      
      1. <ods-hubspot-form
        2.        portal-id="{string}"
        3.        form-id="{string}">
        4. </ods-hubspot-form>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
portalId| [string]()| The portal ID  
formId| [string]()| The form ID


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| portalId | string | The portal ID |
| formId | string | The form ID |

---
### odsInfiniteScrollResults

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsInfiniteScrollResults widget displays the results of a query inside an infinite scroll list. It uses the HTML template inside the widget tag and repeats it for each result.

If used with a Catalog Context, for each result, the following AngularJS variables are available:

  * item.datasetid: Dataset identifier of the dataset
  * item.metas: An object holding the key/values of metadata for this dataset



If used with a Dataset Context, for each result, the following AngularJS variables are available:

  * item.datasetid: Dataset identifier of the dataset this record belongs to
  * item.fields: An object holding all the key/values for the record
  * item.geometry: if the record contains geometrical information, this object is present and holds its GeoJSON representation




#### Usage

as attribute
      
      1. <ANY ods-infinite-scroll-results
        2.      ods-results-context="{CatalogContext|DatasetContext}"
        3.      scroll-top-when-refresh="{boolean}"
        4.      list-class="{string}"
        5.      result-class="{string}"
        6.      [no-results-message]="{string}"
        7.      [no-more-results-message]="{string}"
        8.      [no-data-message]="{string}">
        9.    ...
        10. </ANY>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
odsResultsContext| [CatalogContext]()[DatasetContext]()| Catalog Context or Dataset Context to use  
scrollTopWhenRefresh| [boolean]()| If the context parameters change (which will probably change the results), the widget scrolls to the top of the window. _(default: false)_  
listClass| [string]()| A class (or classes) that will be applied to the list of result _(default: none)_  
resultClass| [string]()| A class (or classes) that will be applied to each result _(default: none)_  
[noResultsMessage]| [string]()| A sentence that will be displayed if there are no results  
[noMoreResultsMessage]| [string]()| A sentence that will be displayed if there are no more results to fetch  
[noDataMessage]| [string]()| A sentence that will be displayed if the context has no content at all


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| odsResultsContext | CatalogContextDatasetContext | Catalog ContextorDataset Contextto use |
| scrollTopWhenRefresh | boolean | If the context parameters change (which will probably change the results), the widget scrolls to the top of the window.(default: false) |
| listClass | string | A class (or classes) that will be applied to the list of result(default: none) |
| resultClass | string | A class (or classes) that will be applied to each result(default: none) |
| [noResultsMessage] | string | A sentence that will be displayed if there are no results |
| [noMoreResultsMessage] | string | A sentence that will be displayed if there are no more results to fetch |
| [noDataMessage] | string | A sentence that will be displayed if the context has no content at all |

---
### odsLastDatasetsFeed

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsLastDatasetsFeed widget displays the last datasets of a catalog based on the _modified_ metadata. By default, the widget displays the last five datasets.


#### Usage

as element:
      
      1. <ods-last-datasets-feed
        2.        context="{CatalogContext}">
        3. </ods-last-datasets-feed>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
context| [CatalogContext]()| Catalog Context to use


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| context | CatalogContext | Catalog Contextto use |

---
### odsLastReusesFeed

**Module:** `ods-widgets`
**Type:** Directive

#### Description

This widget displays the last five reuses published on a domain.

It is possible to customize the template used to display each reuse by adding HTML inside the widget's tag. The following variables are available:

  * `reuse.url`: URL to the reuse's dataset page
  * `reuse.title`: Title of the reuse
  * `reuse.thumbnail`: URL to the thumbnail of the reuse
  * `reuse.description`: Description of the reuse
  * `reuse.created_at`: ISO datetime of reuse's original submission (can be used as `reuse.created_at|moment:'LLL'` to format it)
  * `reuse.dataset.title`: Title of the reuse's dataset
  * `reuse.user.last_name`: Last name of the reuse's submitter
  * `reuse.user.first_name`: First name of the reuse's submitter




#### Usage

as element:
      
      1. <ods-last-reuses-feed
        2.        context="{CatalogContext}"
        3.        max="{number}"
        4.        external-links="{boolean}">
        5. </ods-last-reuses-feed>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
context| [CatalogContext]()| Catalog Context to use  
max| [number]()| Maximum number of reuses to show _(default: 5)_  
externalLinks| [boolean]()| Clicking on the reuses' titles or images will directly redirect to the reuse. Otherwise, by default, it will redirect to the dataset. _(default: false)_


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| context | CatalogContext | Catalog Contextto use |
| max | number | Maximum number of reuses to show(default: 5) |
| externalLinks | boolean | Clicking on the reuses' titles or images will directly redirect to the reuse. Otherwise, by default, it will redirect to the dataset.(default: false) |

---
### odsLegend

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsLegend widget displays a map legend computed with the color gradient structure from the odsColorGradient widget. The `steps` display mode is a legend with different steps based on the range of values. Each step has its own color and value range. The `linear` display mode is a single color gradient from the minimum to the maximum value.

Note: You can use the `steps` display mode only if the ods-color-gradient-nb-classes option has been provided to the odsColorGradient widget.


#### Usage

as element:
      
      1. <ods-legend
        2.        color-gradient="{object}"
        3.        title="{string}"
        4.        subtitle="{string}"
        5.        no-value-color="{string}"
        6.        decimal-precision="{integer}"
        7.        display="{string}">
        8. </ods-legend>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
colorGradient| [object]()| An object providing colors, values, and a range of value. It also provides the number of classes for the `steps` display mode.  
title| [string]()| Legend title  
subtitle| [string]()| Legend sub-title _(default: '')_  
noValueColor| [string]()| Displays another step or square with the provided default color. The authorized values are any HTML color code. _(default: undefined)_  
decimalPrecision| [integer]()| Sets the decimal values precision. _(default: 0)_  
display| [string]()| Display mode. The authorized values are 'steps' and 'linear'. _(default: linear)_


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| colorGradient | object | An object providing colors, values, and a range of value. It also provides the number of classes for thestepsdisplay mode. |
| title | string | Legend title |
| subtitle | string | Legend sub-title(default: '') |
| noValueColor | string | Displays another step or square with the provided default color. The authorized values are any HTML color code.(default: undefined) |
| decimalPrecision | integer | Sets the decimal values precision.(default: 0) |
| display | string | Display mode. The authorized values are 'steps' and 'linear'.(default: linear) |

---
### odsMap

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsMap widget allows to build a map visualization and display data through various modes that can be composed of several dynamic layers, each being based on a Dataset Context.

odsMap is a base widget. Used on its own, it can only display a simple map with default configurations.
      
      1. <!-- Displays a map of Paris using the data from mycontext and an automatic visualization mode -->
        2. <ods-map context="mycontext" location="12,48.85218,2.36996"></ods-map>
    
    

odsMap can be combined with two related map widgets to create more complex maps and fully configure their modes and behaviors.

  * odsMapLayer, allows to declare a layer of data to display on the map
  * odsMapLayerGroup, allows to declare a group of layers



In its fullest form, a map visualization would then be composed of several layers organized in groups. For more information on how to use and configure the odsMapLayer and odsMapLayerGroup widgets, see the odsMapLayer and odsMapLayerGroup documentation.
      
      1. <ods-map ...>
        2.    <ods-map-layer-group ...>
        3.       <ods-map-layer ...></ods-map-layer>
        4.       <ods-map-layer ...></ods-map-layer>
        5.    </ods-map-layer-group>
        6.    <ods-map-layer-group ...>
        7.       <ods-map-layer ...></ods-map-layer>
        8.    </ods-map-layer-group>
        9. </ods-map>
    
    

odsMap, when used for a complex map visualization, is mostly used to set the basic configurations of the map (e.g., basemap, location). odsMap also helps set all map-controlling options, such as zoom configurations, buttons, search bar display, and groups and layers behavior control.


#### Usage

as element:
      
      1. <ods-map
        2.        context="{DatasetContext}"
        3.        location="{string}"
        4.        basemap="{string}"
        5.        min-zoom="{integer}"
        6.        max-zoom="{integer}"
        7.        scroll-wheel-zoom="{boolean}"
        8.        static-map="{boolean}"
        9.        no-refit="{boolean}"
        10.        toolbar-geolocation="{boolean}"
        11.        auto-geolocation="{boolean}"
        12.        toolbar-drawing="{boolean}"
        13.        toolbar-fullscreen="{boolean}"
        14.        display-control="{boolean}"
        15.        display-control-single-layer="{boolean}"
        16.        ods-auto-resize="{boolean}"
        17.        search-box="{boolean}"
        18.        display-legend="{boolean}"
        19.        sync-to-url="{boolean}"
        20.        sync-to-object="{Object}">
        21. </ods-map>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
context| [DatasetContext]()|  _(mandatory)_ Dataset Context to use. If the **context** parameter is managed with odsMapLayer, it should not be configured for odsMap.  
location| [string]()| Controls the default location of the map upon initialization. The value must be set under the following format: `zoom,latitude,longitude`. For example, if you want to have a map centered on Paris, France, you should use `12,48.85218,2.36996`. By default, if a location is not specified, the map will try to fit all the displayed data when initializing.  
basemap| [string]()| Identifier of the basemap to use by default, as defined in ODSWidgetsConfig.basemaps. By default, the first available basemap will be used.  
minZoom| [integer]()| Limits the map to a minimum zoom value. By default, this is defined by the minimum zoom of the basemap. _(default: none)_  
maxZoom| [integer]()| Limits the map to a maximum zoom value. By default, this is defined by the maximum zoom of the basemap. _(default: none)_  
scrollWheelZoom| [boolean]()| When set to `true`, scrolling the mouse wheel over the map can be used to zoom in or zoom out. _(default: true)_  
staticMap| [boolean]()| When set to `true`, the map can't be zoomed in/out or moved. Markers are still clickable. _(default: false)_  
noRefit| [boolean]()| By default, the map refits its view whenever the displayed data changes. When set to `true`, the map stays at the same location. _(default: false)_  
toolbarGeolocation| [boolean]()| When set to `true`, the "geolocate" button is displayed in the map's toolbar. _(default: true)_  
autoGeolocation| [boolean]()| When set to `true`, the geolocation, which centers and zooms the map on the user's location, is automatically done upon initialization. `autoGeolocation` is only available when there is no **location** parameter set for the widget. Caution: location sharing must be allowed priorly for Firefox users when multiple odsMap widget are set with `autoGeolocation=true` on the same page. _(default: false)_  
toolbarDrawing| [boolean]()| When set to `false`, the drawing tools to draw filter areas are not displayed in the map's toolbar. _(default: true)_  
toolbarFullscreen| [boolean]()| When set to `false`, the "fullscreen" button is not displayed in the map's toolbar. _(default: true)_  
displayControl| [boolean]()| When set to `true`, displays a control to choose whether groups or single datasets outside groups should be displayed, using toggle buttons. Note: it shouldn't be combined with the usage of **showIf** on odsMapLayer, as it will lead to inconsistencies in the user interface. _(default: false)_  
displayControlSingleLayer| [boolean]()| When set to `true`, only one layer is displayed at a time using the control of groups and single datasets display. _(default: false)_  
odsAutoResize| [boolean]()| For more information, see Auto Resize.  
searchBox| [boolean]()| When set to `true`, a search box is displayed on the map so that users can jump to another location through a search or search specific data on the map. _(default: false)_  
displayLegend| [boolean]()| When set to `true`, a caption is displayed in the bottom right corner of the map. _(default: true)_  
syncToUrl| [boolean]()| When set to `true`, the settings of the **location** and **basemap** parameters are used in the page's URL. _(default: none)_  
syncToObject| [Object]()| An object updated by the map's settings for the **location** and **basemap** parameters corresponding to new changes of location and basemap. _(default: none)_


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| context | DatasetContext | (mandatory)Dataset Contextto use. If thecontextparameter is managed withodsMapLayer, it should not be configured for odsMap. |
| location | string | Controls the default location of the map upon initialization. The value must be set under the following format:zoom,latitude,longitude. For example, if you want to have a map centered on Paris, France, you should use12,48.85218,2.36996. By default, if a location is not specified, the map will try to fit all the displayed data when initializing. |
| basemap | string | Identifier of the basemap to use by default, as defined inODSWidgetsConfig.basemaps. By default, the first available basemap will be used. |
| minZoom | integer | Limits the map to a minimum zoom value. By default, this is defined by the minimum zoom of the basemap.(default: none) |
| maxZoom | integer | Limits the map to a maximum zoom value. By default, this is defined by the maximum zoom of the basemap.(default: none) |
| scrollWheelZoom | boolean | When set totrue, scrolling the mouse wheel over the map can be used to zoom in or zoom out.(default: true) |
| staticMap | boolean | When set totrue, the map can't be zoomed in/out or moved. Markers are still clickable.(default: false) |
| noRefit | boolean | By default, the map refits its view whenever the displayed data changes. When set totrue, the map stays at the same location.(default: false) |
| toolbarGeolocation | boolean | When set totrue, the "geolocate" button is displayed in the map's toolbar.(default: true) |
| autoGeolocation | boolean | When set totrue, the geolocation, which centers and zooms the map on the user's location, is automatically done upon initialization.autoGeolocationis only available when there is nolocationparameter set for the widget.Caution: location sharing must be allowed priorly for Firefox users when multiple odsMap widget are set withautoGeolocation=trueon the same page.(default: false) |
| toolbarDrawing | boolean | When set tofalse, the drawing tools to draw filter areas are not displayed in the map's toolbar.(default: true) |
| toolbarFullscreen | boolean | When set tofalse, the "fullscreen" button is not displayed in the map's toolbar.(default: true) |
| displayControl | boolean | When set totrue, displays a control to choose whether groups or single datasets outside groups should be displayed, using toggle buttons.Note: it shouldn't be combined with the usage ofshowIfonodsMapLayer, as it will lead to inconsistencies in the user interface.(default: false) |
| displayControlSingleLayer | boolean | When set totrue, only one layer is displayed at a time using the control of groups and single datasets display.(default: false) |
| odsAutoResize | boolean | For more information, seeAuto Resize. |
| searchBox | boolean | When set totrue, a search box is displayed on the map so that users can jump to another location through a search or search specific data on the map.(default: false) |
| displayLegend | boolean | When set totrue, a caption is displayed in the bottom right corner of the map.(default: true) |
| syncToUrl | boolean | When set totrue, the settings of thelocationandbasemapparameters are used in the page's URL.(default: none) |
| syncToObject | Object | An object updated by the map's settings for thelocationandbasemapparameters corresponding to new changes of location and basemap.(default: none) |

---
### odsMapLayer

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsMapLayer widget allows to declare the data layers that can be displayed on a map visualization. odsMapLayer is one of the map-related widgets that can only be used based on odsMap, the primary map-related widgets. For more information on odsMap, see the documentation for this widget.

A map visualization can comprise several data layers, which are dynamic. In other words, if the context changes, the layer is refreshed and displays the new relevant data.

Each data layer is based on a context and can have its own display mode and configurations.
      
      1. <ods-map>
        2.     <ods-map-layer context="mycontext" color="#FF0000" display="clusters"></ods-map-layer>
        3.     <ods-map-layer context="mycontext2" display="heatmap"></ods-map-layer>
        4.     <ods-map-layer context="mycontext3" display="raw" color="#0000FF"></ods-map-layer>
        5. </ods-map>
    
    

**Layers display modes**

Map visualizations can either display:

  * the layer data itself (i.e., each point is a record from the dataset), or
  * an aggregation of data (i.e., each point is the result of an aggregation function).



Several display modes are available (see **display** parameter in the table below). However, only some of them support aggregation functions: `aggregation`, `heatmap`, and `clustersforced`.

Aggregation functions are specified in the odsMapLayer widget through 2 parameters: **function** and **expression** , which define the value used for the function (usually, the name of a field). For more information, see the "Parameters" table.
      
      1. <ods-map>
        2.     <!-- Display a heatmap of the average value -->
        3.     <ods-map-layer context="mycontext" display="heatmap" expression="value" function="AVG"></ods-map-layer>
        4. </ods-map>
    
    

**Layers display color configurations**

Apart from `heatmap`, all display modes support color configuration. Three configuration types are available, depending on the display mode:

  * `color`: a color, as an hex code (#FF0F05) or a CSS color name (e.g., "red"). Available for any display mode.
  * `colorScale`: the name of a [ColorBrewer](http://colorbrewer2.org/) scheme (e.g., "YlGnBu"). Available only for `aggregation`.
  * `colorRanges`: a series of colors and ranges separated by a semicolon, to decide a color depending on a value. For example "red;20;orange;40;#00CE00" colors anything between 20 and 40 in orange, below 20 in red, and above 40 in a custom hex color.



It can be combined with a decimal or integer field name in `colorByField` to configure which field will be used to decide on the color (for `raw`) or with `function` and `expression` to determine the calculation used for the color (for `aggregation`).

Available for `raw` and `aggregation` display modes.

An additional `colorFunction` property can contain the `log` value to use logarithmic scales (instead of the default linear scale) for generating the color scale.

Available for `aggregation` and with `color` and `colorScale` display modes, or when none is specified.

On top of color configuration, the icon used as a marker on the map can be configured through the `picto` property. The property supports the keywords listed in the [Pictograms reference documentation](https://userguide.huwise.com/en/articles/2042498).

When displaying shapes, `borderColor` and `opacity` can be used to configure the color of the shape border and the opacity of the shape's fill.

**Layers zoom and hide & show configurations**

Layers can be hidden or shown depending on the configuration of the `showIf` parameter, which functions similarly to Angular's `ngIf`.
      
      1. <ods-map>
        2.     <ods-map-layer context="mycontext" color="#FF0000" display="clusters"></ods-map-layer>
        3.     <ods-map-layer context="mycontext2" display="heatmap" show-if="showHeatmap"></ods-map-layer>
        4. </ods-map>
    
    

Layers can also be configured to only be visible between certain zoom levels, using the `showZoomMin` and/or `showZoomMax` parameters.
      
      1. <ods-map>
        2.     <!-- This layer is only visible up to zoom 8 -->
        3.     <ods-map-layer context="mycontext1" show-zoom-max="8"></ods-map-layer>
        4.     <!-- This layer appears between zoom 9 and 14 -->
        5.     <ods-map-layer context="mycontext2" show-zoom-min="9" show-zoom-max="14"></ods-map-layer>
        6.     <!-- This layer is visible starting at zoom 15 -->
        7.     <ods-map-layer context="mycontext3" show-zoom-min="15"></ods-map-layer>
        8. </ods-map>
    
    

**Tooltips**

By default, tooltips show the values associated with a point or shape in a simple template. Custom HTML tooltip templates can be added inside the `<ods-map-layer></ods-map-layer>` tag. The custom template is AngularJS-enabled and will be provided with a `record` object; this object contains a `fields` object with all the values associated with the clicked point or shape.
      
      1. <ods-map location="12,48.86167,2.34146">
        2.     <ods-map-layer context="mycontext">
        3.         <div>my value is: {{record.fields.myvalue}}</div>
        4.     </ods-map-layer>
        5. </ods-map>
    
    

In case the tooltip is not relevant for the map visualization, it can be disabled them using the **tooltipDisabled** parameter set on `true`.
      
      1. <ods-map>
        2.     <ods-map-layer context="mycontext" tooltip-disabled="true"></ods-map-layer>
        3. </ods-map>
    
    

If the map visualization displays multiple points or shapes that are stacked, it is possible to configure the order in which the items will be displayed in the tooltip, using `tooltipSort` and the name of a field, prefixed by `-` to have a reversed sort. Note: by default, numeric fields are sorted in decreasing order, date and datetime are sorted chronologically, and text fields are sorted alphanumerically.
      
      1. <ods-map>
        2.     <!-- Reverse sort on 'field' -->
        3.     <ods-map-layer context="mycontext" tooltip-sort="-field"></ods-map-layer>
        4. </ods-map>
    
    

**Refine-on-click map configuration**

If a layer is displayed as `raw` or `aggregation`, it can be configured so that a click on an item triggers a refine on another context, using **refineOnClickContext**.

One or more contexts can be defined:
      
      1. <ods-map>
        2.     <ods-map-layer context="mycontext" refine-on-click-context="mycontext2"></ods-map-layer>
        3.     <ods-map-layer context="mycontext3" refine-on-click-context="[mycontext4, mycontext5]"></ods-map-layer>
        4. </ods-map>
    
    

By default, the filter occurs on geometry. For example, clicking on a shape filters the other context on the area.

It is also possible to trigger a refine on specific fields, using **refineOnClickMapField** to configure the name of the field to get the value from, and **refineOnClickContextField** to configure the name of the field of the other context to refine on. If there are 2 or more contexts, it is possible to configure the fields by indicating the context in the name of the property, as `refineOnClick[context]MapField` and `refineOnClick[context]ContextField`.
      
      1. <ods-map>
        2.     <ods-map-layer context="mycontext"
        3.                    refine-on-click-context="[mycontext, mycontext2]"
        4.                    refine-on-click-mycontext-map-field="field1"
        5.                    refine-on-click-mycontext-context-field="field2"
        6.                    refine-on-click-mycontext2-map-field="field3"
        7.                    refine-on-click-mycontext2-context-field="field4"></ods-map-layer>
        8. </ods-map>
    
    


#### Usage

as element:
      
      1. <ods-map-layer
        2.        context="{DatasetContext}"
        3.        show-if="{expression}"
        4.        show-zoom-min="{number}"
        5.        show-zoom-max="{number}"
        6.        display="{string}"
        7.        function="{string}"
        8.        expression="{expression}"
        9.        color="{string}"
        10.        border-color="{string}"
        11.        border-size="{number}"
        12.        border-pattern="{string}"
        13.        border-opacity="{number}"
        14.        shape-opacity="{number}"
        15.        point-opacity="{number}"
        16.        line-width="{number}"
        17.        color-categories="{objet}"
        18.        color-categories-other="{string}"
        19.        color-undefined="{string}"
        20.        color-out-of-bounds="{string}"
        21.        color-numeric-ranges="{string}"
        22.        color-numeric-range-min="{number}"
        23.        color-gradient="{string}"
        24.        color-by-field="{string}"
        25.        radius="{number}"
        26.        size="{number}"
        27.        size-min="{number}"
        28.        size-max="{number}"
        29.        size-function="{string}"
        30.        picto="{string}"
        31.        show-marker="{boolean}"
        32.        tooltip-sort="{string}"
        33.        tooltip-disabled="{boolean}"
        34.        caption="{boolean}"
        35.        caption-title="{string}"
        36.        caption-picto-color="{string}"
        37.        caption-picto-icon="{string}"
        38.        title="{string}"
        39.        description="{string}"
        40.        exclude-from-refit="{boolean}"
        41.        refine-on-click-context="{string}"
        42.        refine-on-click-map-field="{string}"
        43.        refine-on-click-context-field="{string}"
        44.        refine-on-click-replace-refine="{boolean}">
        45. </ods-map-layer>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
context| [DatasetContext]()|  _(mandatory)_ Dataset Context to use  
showIf| [expression]()| AngularJS expression to evaluate: if it evaluates to true, the layer is visible. _(default: none)_  
showZoomMin| [number]()| Makes the layer visible only if the zoom level is superior or equal to the value. _(default: none)_  
showZoomMax| [number]()| Makes the layer visible only if the zoom level is inferior or equal to the value. _(default: none)_  
display| [string]()| Map mode:

  * `auto`: automatically chooses the best map mode to easily display the data, based on the number of points and type of geometry
  * `heatmap`: displays the data as a heatmap, i.e. a density of points represented by a color intensity variation. It can also be based on the result of an aggregation function.
  * `categories`: based on a text field value, categorizes and colors the data
  * `choropleth`: based on a number field or aggregation, colors the data using a color scale
  * `clusters`: spatially groups the data in clusters ; each cluster displays the number of points it contains. When at maximum zoom, all points are shown.
  * `clustersforced`: spatially aggregates the data in clusters ; the number displayed on the cluster is the result of an aggregation function.
  * `raw`: displays the data directly without clustering or organizing them. This mode should not be used for large datasets (i.e., datasets with more than 5,000 points to display), as it may freeze the user's browser.
  * `aggregation`: data is aggregated based on a geo shape (e.g., 2 records with the exact same shape associated). By default, the color represents the number of aggregated records, but it can be the result of an aggregation function. This mode supports aggregating the context using a join with another context that contains geometrical shapes: use a `joinContext` property, and `localKey` and `remoteKey` to configure the field names of the local and joined datasets. It is also possible to configure one of the fields from the "remote" dataset, for them to be displayed when the mouse hovers the shapes: use `hoverField` and the name of a field to do so.

_(default: auto)_  
function| [string]()| For the `heatmap`, `choropleth`, and `clusters` modes only–function used to aggregate the data:

  * AVG: average
  * COUNT
  * MIN: minimum
  * MAX: maximum
  * STDDEV: standard deviation
  * SUM

_(default: none)_  
expression| [expression]()| Expression used to aggregate the data. This parameter is not required when the function is COUNT. _(default: none)_  
color| [string]()| Color of the displayed shapes and markers _(default: none)_  
borderColor| [string]()| Color of the shapes' borders _(default: white)_  
borderSize| [number]()| The width of the shapes' borders, in pixels _(default: 1)_  
borderPattern| [string]()| Pattern of the shapes' borders:

  * `solid`
  * `long-dashes`
  * `medium-dashes`
  * `short-dashes`
  * `dots`
  * `short-dot`
  * `short-dot-dot`
  * `medium-short`

_(default: solid)_  
borderOpacity| [number]()| Opacity of the shapes' borders. The value must be between `0` (transparent) and `1` (opaque). _(default: 1)_  
shapeOpacity| [number]()| Opacity of the shapes. The value must be between `0` (transparent) and `1` (opaque). _(default: 0.5)_  
pointOpacity| [number]()| Opacity of the markers. The value must be between `0` (transparent) and `1` (opaque). _(default: 1)_  
lineWidth| [number]()| The width of the lines, in pixels. Only applicable for "line" type shapes. _(default: 5)_  
colorCategories| [objet]()| For the `categories` mode only–object that links textual values and colors (e.g., `{'Paris': '#FF0000', 'Nantes: '#00FF00'}`). _(default: none)_  
colorCategoriesOther| [string]()| For the `categories` mode only–default color for values that were not originally taken into account by the `color-categories` object. _(default: none)_  
colorUndefined| [string]()| For the `choropleth` mode only–default color for the `undefined` values. _(default: none)_  
colorOutOfBounds| [string]()| For the `choropleth` mode only–default color for values out of the expected `color-numeric-ranges` scale. _(default: none)_  
colorNumericRanges| [string]()| For the `choropleth` mode only–color scale used (e.g., `{'0': '#FF0000', '1': '#FFFF00'}`). The key is the upper bound used for this color (e.g., still using the previous example, it would be #FF0000 until 0, then #FFFF00 until 1, etc.) _(default: none)_  
colorNumericRangeMin| [number]()| For the `choropleth` mode only–minimum bound used. Any value below that bound will be considered out of the scale, and will use the color of the `color-out-of-bounds` parameter. _(default: none)_  
colorGradient| [string]()| For the `heatmap` mode only–object that links upper numeric bounds and colors (e.g., `{0.2: '#FF0000', 1: '#00FF00'}`) _(default: none)_  
colorByField| [string]()| For categories and choropleth modes only - Field used to choose the color _(default: none)_  
radius| [number]()| For the `heatmap` mode only–width of the perimeter _(default: 4)_  
size| [number]()| For markers, 7 for pictograms–size of the markers _(default: 4)_  
sizeMin| [number]()| For the `clusters` mode only–minimum size of the clusters _(default: 3)_  
sizeMax| [number]()| For the `clusters` mode only–maximum size of the clusters _(default: 5)_  
sizeFunction| [string]()| For the `clusters` mode only–calculation function of the clusters size:

  * `linear`
  * `log` (logarithmic)

_(default: none)_  
picto| [string]()| Pictogram used for the markers _(default: none)_  
showMarker| [boolean]()| When set to `true`, displays a marker around the pictogram. _(default: none)_  
tooltipSort| [string]()| Identifier of the field used to sort tooltips that represent several records for the same point or shape. Note that `-` before the name of the sorting method indicates that the sorting will be descending instead of ascending. By default, numeric fields are sorted in decreasing order, date and datetime are sorted chronologically, and text fields are sorted alphanumerically.  
tooltipDisabled| [boolean]()| When set to `true`, clicking on a point or shape does not display the associated tooltip. _(default: none)_  
caption| [boolean]()| When set to `true`, displays a caption for the map layer in the bottom right corner of the map. _(default: none)_  
captionTitle| [string]()| Title of the map layer caption. _(default: none)_  
captionPictoColor| [string]()| Color used for the caption's pictogram _(default: none)_  
captionPictoIcon| [string]()| Pictogram used in the caption _(default: none)_  
title| [string]()| Title used in the map layer's control selection _(default: none)_  
description| [string]()| Description used in the map layer's control selection _(default: none)_  
excludeFromRefit| [boolean]()| When set to `true`, the calculation that rezooms the map when filters or data change does not take the map layer into account. _(default: none)_  
refineOnClickContext| [string]()| Name, or list of names separated by commas (`[ctx1, ctx2]`) of contexts that should be refined when clicking on a point or shape of the map layer. _(default: none)_  
refineOnClickMapField| [string]()| (or `refine-on-click-CONTEXTNAME-map-field` if more than one context) - Field of the map layer that is used to retrieve the value used for the refine _(default: none)_  
refineOnClickContextField| [string]()| (or `refine-on-click-CONTEXTNAME-context-field` if more than one context) - Field used in the context of the refine (`refine.FIELDNAME=VALUE`) _(default: none)_  
refineOnClickReplaceRefine| [boolean]()| (or `refine-on-click-CONTEXTNAME-replace-refine` if more than one context) - When set to `true`, each click replaces the previous refine instead of adding to it. _(default: none)_


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| context | DatasetContext | (mandatory)Dataset Contextto use |
| showIf | expression | AngularJS expression to evaluate: if it evaluates to true, the layer is visible.(default: none) |
| showZoomMin | number | Makes the layer visible only if the zoom level is superior or equal to the value.(default: none) |
| showZoomMax | number | Makes the layer visible only if the zoom level is inferior or equal to the value.(default: none) |
| display | string | Map mode:auto: automatically chooses the best map mode to easily display the data, based on the number of points and type of geometryheatmap: displays the data as a heatmap, i.e. a density of points represented by a color intensity variation. It can also be based on the result of an aggregation function.categories: based on a text field value, categorizes and colors the datachoropleth: based on a number field or aggregation, colors the data using a color scaleclusters: spatially groups the data in clusters ; each cluster displays the number of points it contains. When at maximum zoom, all points are shown.clustersforced: spatially aggregates the data in clusters ; the number displayed on the cluster is the result of an aggregation function.raw: displays the data directly without clustering or organizing them. This mode should not be used for large datasets (i.e., datasets with more than 5,000 points to display), as it may freeze the user's browser.aggregation: data is aggregated based on a geo shape (e.g., 2 records with the exact same shape associated). By default, the color represents the number of aggregated records, but it can be the result of an aggregation function. This mode supports aggregating the context using a join with another context that contains geometrical shapes: use ajoinContextproperty, andlocalKeyandremoteKeyto configure the field names of the local and joined datasets. It is also possible to configure one of the fields from the "remote" dataset, for them to be displayed when the mouse hovers the shapes: usehoverFieldand the name of a field to do so.(default: auto) |
| function | string | For theheatmap,choropleth, andclustersmodes only–function used to aggregate the data:AVG: averageCOUNTMIN: minimumMAX: maximumSTDDEV: standard deviationSUM(default: none) |
| expression | expression | Expression used to aggregate the data. This parameter is not required when the function is COUNT.(default: none) |
| color | string | Color of the displayed shapes and markers(default: none) |
| borderColor | string | Color of the shapes' borders(default: white) |
| borderSize | number | The width of the shapes' borders, in pixels(default: 1) |
| borderPattern | string | Pattern of the shapes' borders:solidlong-dashesmedium-dashesshort-dashesdotsshort-dotshort-dot-dotmedium-short(default: solid) |
| borderOpacity | number | Opacity of the shapes' borders. The value must be between0(transparent) and1(opaque).(default: 1) |
| shapeOpacity | number | Opacity of the shapes. The value must be between0(transparent) and1(opaque).(default: 0.5) |
| pointOpacity | number | Opacity of the markers. The value must be between0(transparent) and1(opaque).(default: 1) |
| lineWidth | number | The width of the lines, in pixels. Only applicable for "line" type shapes.(default: 5) |
| colorCategories | objet | For thecategoriesmode only–object that links textual values and colors (e.g.,{'Paris': '#FF0000', 'Nantes: '#00FF00'}).(default: none) |
| colorCategoriesOther | string | For thecategoriesmode only–default color for values that were not originally taken into account by thecolor-categoriesobject.(default: none) |
| colorUndefined | string | For thechoroplethmode only–default color for theundefinedvalues.(default: none) |
| colorOutOfBounds | string | For thechoroplethmode only–default color for values out of the expectedcolor-numeric-rangesscale.(default: none) |
| colorNumericRanges | string | For thechoroplethmode only–color scale used (e.g.,{'0': '#FF0000', '1': '#FFFF00'}). The key is the upper bound used for this color (e.g., still using the previous example, it would be #FF0000 until 0, then #FFFF00 until 1, etc.)(default: none) |
| colorNumericRangeMin | number | For thechoroplethmode only–minimum bound used. Any value below that bound will be considered out of the scale, and will use the color of thecolor-out-of-boundsparameter.(default: none) |
| colorGradient | string | For theheatmapmode only–object that links upper numeric bounds and colors (e.g.,{0.2: '#FF0000', 1: '#00FF00'})(default: none) |
| colorByField | string | For categories and choropleth modes only - Field used to choose the color(default: none) |
| radius | number | For theheatmapmode only–width of the perimeter(default: 4) |
| size | number | For markers, 7 for pictograms–size of the markers(default: 4) |
| sizeMin | number | For theclustersmode only–minimum size of the clusters(default: 3) |
| sizeMax | number | For theclustersmode only–maximum size of the clusters(default: 5) |
| sizeFunction | string | For theclustersmode only–calculation function of the clusters size:linearlog(logarithmic)(default: none) |
| picto | string | Pictogram used for the markers(default: none) |
| showMarker | boolean | When set totrue, displays a marker around the pictogram.(default: none) |
| tooltipSort | string | Identifier of the field used to sort tooltips that represent several records for the same point or shape.Note that-before the name of the sorting method indicates that the sorting will be descending instead of ascending.By default, numeric fields are sorted in decreasing order, date and datetime are sorted chronologically, and text fields are sorted alphanumerically. |
| tooltipDisabled | boolean | When set totrue, clicking on a point or shape does not display the associated tooltip.(default: none) |
| caption | boolean | When set totrue, displays a caption for the map layer in the bottom right corner of the map.(default: none) |
| captionTitle | string | Title of the map layer caption.(default: none) |
| captionPictoColor | string | Color used for the caption's pictogram(default: none) |
| captionPictoIcon | string | Pictogram used in the caption(default: none) |
| title | string | Title used in the map layer's control selection(default: none) |
| description | string | Description used in the map layer's control selection(default: none) |
| excludeFromRefit | boolean | When set totrue, the calculation that rezooms the map when filters or data change does not take the map layer into account.(default: none) |
| refineOnClickContext | string | Name, or list of names separated by commas ([ctx1, ctx2]) of contexts that should be refined when clicking on a point or shape of the map layer.(default: none) |
| refineOnClickMapField | string | (orrefine-on-click-CONTEXTNAME-map-fieldif more than one context) - Field of the map layer that is used to retrieve the value used for the refine(default: none) |
| refineOnClickContextField | string | (orrefine-on-click-CONTEXTNAME-context-fieldif more than one context) - Field used in the context of the refine (refine.FIELDNAME=VALUE)(default: none) |
| refineOnClickReplaceRefine | boolean | (orrefine-on-click-CONTEXTNAME-replace-refineif more than one context) - When set totrue, each click replaces the previous refine instead of adding to it.(default: none) |

---
### odsMapLayerGroup

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsMapLayerGroup widget allows to declare a group of layers, which are declared through the odsMapLayer widget. odsMapLayerGroup is one of the map-related widgets that can only be used based on odsMap, the primary map-related widgets. For more information on odsMap, see the documentation for this widget.


#### Usage

as element:
      
      1. <ods-map-layer-group
        2.        title="{string}"
        3.        description="{string}"
        4.        picto-color="{string}"
        5.        picto-icon="{string}"
        6.        displayed="{boolean}">
        7. </ods-map-layer-group>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
title| [string]()|  _(mandatory)_ Title of the group of layers  
description| [string]()| Description of the group of layers _(default: none)_  
pictoColor| [string]()| Color of the pictogram for the group of layers', in the following format: `#000000` _(default: #000000)_  
pictoIcon| [string]()| Name of pictogram for the group of layers _(default: none)_  
displayed| [boolean]()| When set to `true`, the group of layers is displayed by default. _(default: true)_


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| title | string | (mandatory)Title of the group of layers |
| description | string | Description of the group of layers(default: none) |
| pictoColor | string | Color of the pictogram for the group of layers', in the following format:#000000(default: #000000) |
| pictoIcon | string | Name of pictogram for the group of layers(default: none) |
| displayed | boolean | When set totrue, the group of layers is displayed by default.(default: true) |

---
### odsMediaGallery

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsMediaGallery widget displays an image gallery of a dataset containing media with thumbnails (images, PDF files, etc.) with infinite scroll. You can use the Widget Tooltip directive to customize the detail view appearing when selecting a thumbnail.


#### Usage

as element:
      
      1. <ods-media-gallery
        2.        context="{DatasetContext}"
        3.        displayed-fields="{string}"
        4.        image-fields="{string}"
        5.        [ods-widget-tooltip]="{string}"
        6.        [ods-auto-resize]="{boolean}"
        7.        [refine-on-click]="{boolean}">
        8. </ods-media-gallery>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
context| [DatasetContext]()| Dataset Context to use  
displayedFields| [string]()| A comma-separated list of fields to display in the details for each thumbnail. If no value is specified, the options configured for the dataset are used or all fields if nothing configured. _(default: all)_  
imageFields| [string]()| A comma-separated list of fields to display in the gallery as thumbnails. If no value is specified, the options configured for the dataset are used or all media fields if nothing is configured. _(default: all)_  
[odsWidgetTooltip]| [string]()| For more information, see Widget Tooltip.  
[odsAutoResize]| [boolean]()| For more information, see Auto Resize.  
[refineOnClick]| [boolean]()| For more information, see Refine on click. This option takes precedence over the widget tooltip.


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| context | DatasetContext | Dataset Contextto use |
| displayedFields | string | A comma-separated list of fields to display in the details for each thumbnail. If no value is specified, the options configured for the dataset are used or all fields if nothing configured.(default: all) |
| imageFields | string | A comma-separated list of fields to display in the gallery as thumbnails. If no value is specified, the options configured for the dataset are used or all media fields if nothing is configured.(default: all) |
| [odsWidgetTooltip] | string | For more information, seeWidget Tooltip. |
| [odsAutoResize] | boolean | For more information, seeAuto Resize. |
| [refineOnClick] | boolean | For more information, seeRefine on click. This option takes precedence over the widget tooltip. |

---
### odsMostPopularDatasets

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsMostPopularDatasets widget displays the top datasets of a catalog based on the number of downloads. By default, the widget displays the top five datasets.


#### Usage

as element:
      
      1. <ods-most-popular-datasets
        2.        context="{CatalogContext}"
        3.        max="{integer}"
        4.        order-by="{string}">
        5. </ods-most-popular-datasets>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
context| [CatalogContext]()| Catalog Context to use.  
max| [integer]()| Number of datasets to show in the list. _(default: 5)_  
orderBy| [string]()| List order. Datasets can be sorted by most downloaded or popularity. The authorized values are `downloads` and `popularity`. _(default: downloads)_


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| context | CatalogContext | Catalog Contextto use. |
| max | integer | Number of datasets to show in the list.(default: 5) |
| orderBy | string | List order. Datasets can be sorted by most downloaded or popularity. The authorized values aredownloadsandpopularity.(default: downloads) |

---
### odsMostUsedThemes

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsMostUsedThemes widget displays the five most used themes.


#### Usage

as element:
      
      1. <ods-most-used-themes
        2.        context="{CatalogContext}">
        3. </ods-most-used-themes>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
context| [CatalogContext]()| Catalog Context to use


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| context | CatalogContext | Catalog Contextto use |

---
### odsPageRefresh

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsPageRefresh widget can be used to periodically refresh the page.


#### Usage

as element:
      
      1. <ods-page-refresh
        2.        delay="{Number}">
        3. </ods-page-refresh>
    
    

as attribute
      
      1. <ANY ods-page-refresh
        2.      delay="{Number}">
        3.    ...
        4. </ANY>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
delay| [Number]()| The number of milliseconds to wait before refreshing the page. The minimum value is `10000`. _(default: 10000)_


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| delay | Number | The number of milliseconds to wait before refreshing the page. The minimum value is10000.(default: 10000) |

---
### odsPaginationBlock

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsPaginationBlock widget displays a pagination control that you can use to make the context "scroll" through a list of results.

The widget doesn't display results. Therefore, it should be paired with another widget. The widget doesn't control the number of results fetched by the context. The `perPage` parameter should be the same as the `rows` parameter on the context.

If you just want to display results with a pagination system, you can use odsResultEnumerator, which already includes this directive (if the relevant parameter is active on the widget).


#### Usage

as element:
      
      1. <ods-pagination-block
        2.        context="{CatalogContext|DatasetContext}"
        3.        per-page="{number}"
        4.        nofollow="{boolean}"
        5.        [container-identifier]="{string}">
        6. </ods-pagination-block>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
context| [CatalogContext]()[DatasetContext]()| Catalog Context or Dataset Context to use  
perPage| [number]()| Controls the number of results per page. _(default: 10)_  
nofollow| [boolean]()| When set to `true`, all links within the widget (used to change page) will contain a `rel="nofollow"` attribute. It should be used if you don't want search engines to crawl all the pages of your widget. _(default: false)_  
[containerIdentifier]| [string]()| By default, changing the page will trigger a scroll to the top of the window. You can use this parameter to specify the ID of the element that will contain the results (e.g., "my-results") so that the behavior is more precise:

  * If your results are inside a container that is used to vertically scroll the results, the container's scroll will be set at the start.
  * If your results are inside a container that doesn't have a scrollbar, the page itself will scroll to the start of the container. Note: In the second situation, some CSS properties may prevent the widget from understanding that it doesn't have a scrollbar. As a result, the widget won't be able to scroll scrolling to the top of the container. This issue may be caused by the odsPaginationBlock widget slightly overflowing its container, typically because of large fonts or higher line-height settings. In this situation, forcing a height on the widget may fix the issue.




#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| context | CatalogContextDatasetContext | Catalog ContextorDataset Contextto use |
| perPage | number | Controls the number of results per page.(default: 10) |
| nofollow | boolean | When set totrue, all links within the widget (used to change page) will contain arel="nofollow"attribute. It should be used if you don't want search engines to crawl all the pages of your widget.(default: false) |
| [containerIdentifier] | string | By default, changing the page will trigger a scroll to the top of the window. You can use this parameter to specify the ID of the element that will contain the results (e.g., "my-results") so that the behavior is more precise:If your results are inside a container that is used to vertically scroll the results, the container's scroll will be set at the start.If your results are inside a container that doesn't have a scrollbar, the page itself will scroll to the start of the container. Note: In the second situation, some CSS properties may prevent the widget from understanding that it doesn't have a scrollbar. As a result, the widget won't be able to scroll scrolling to the top of the container. This issue may be caused by the odsPaginationBlock widget slightly overflowing its container, typically because of large fonts or higher line-height settings. In this situation, forcing a height on the widget may fix the issue. |

---
### odsPicto

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsPicto widget displays a pictogram specified by a URL or the ID of a SVG to duplicate from the same page, and forces a fill color on it. This element can be styled (height, width, etc.), especially if the pictogram is vectorial (SVG).

Either the `url` or `localId` attributes have to be used.

In the case of `localId`, the recommended use is to include the code of the SVG inside your HTML document, with a `display: none` style attribute at the root, on the `svg` node. This inlined SVG will be duplicated, the `display: none` removed, and this new duplicated and colored SVG will be inserted in place of the odsPicto element.

All parameters expect javascript variables or literals. If you want to provide hardcoded strings, you'll have to wrap them in quotes, as shown in the following example.


#### Usage

as element:
      
      1. <ods-picto
        2.        url="{string}"
        3.        local-id="{string}"
        4.        color="{string}"
        5.        color-by-attribute="{Object}"
        6.        classes="{string}">
        7. </ods-picto>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
url| [string]()| The URL of the SVG or image to display  
localId| [string]()| The ID of the SVG to use in the current page  
color| [string]()| The color to use to fill the SVG  
colorByAttribute| [Object]()| An object containing a mapping between elements within the SVG, and colors. The elements within the SVG with a matching `data-fill-id` attribute take the corresponding color.  
classes| [string]()| The classes to directly apply to the SVG element


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| url | string | The URL of the SVG or image to display |
| localId | string | The ID of the SVG to use in the current page |
| color | string | The color to use to fill the SVG |
| colorByAttribute | Object | An object containing a mapping between elements within the SVG, and colors. The elements within the SVG with a matchingdata-fill-idattribute take the corresponding color. |
| classes | string | The classes to directly apply to the SVG element |

---
### odsPopIn

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsPopIn widget displays a pop-in on the page with the provided content.

You can define the time before displaying the pop-in (the timer start when the widget is loaded). In the content, you can access a `hidePopIn()` function that you can use in an `ng-click`.


#### Usage

as element:
      
      1. <ods-pop-in
        2.        name="{string}"
        3.        title="{string}"
        4.        display-after="{number}"
        5.        display-only-once="{boolean}">
        6. </ods-pop-in>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
name| [string]()| The name of the pop-in, used internally to uniquely reference it (required)  
title| [string]()| The title displayed inside the pop-up windows _(default: '')_  
displayAfter| [number]()| The delay in second before displaying the pop-up window _(default: 10)_  
displayOnlyOnce| [boolean]()| When set to `false`, the pop-up window will be displayed at each browsing session of the user. _(default: true)_


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| name | string | The name of the pop-in, used internally to uniquely reference it (required) |
| title | string | The title displayed inside the pop-up windows(default: '') |
| displayAfter | number | The delay in second before displaying the pop-up window(default: 10) |
| displayOnlyOnce | boolean | When set tofalse, the pop-up window will be displayed at each browsing session of the user.(default: true) |

---
### odsRecordImage

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsRecordImage widget displays an image from a record.


#### Usage

as element:
      
      1. <ods-record-image
        2.        context="{DatasetContext}"
        3.        record="{Object}"
        4.        field="{string}"
        5.        domain-url="{string}">
        6. </ods-record-image>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
context| [DatasetContext]()| Dataset Context to use  
record| [Object]()| Record to take the image from  
field| [string]()|  _(mandatory)_ Field to use.  
domainUrl| [string]()| The base URL of the domain where the dataset can be found. By default, the current domain is used. _(default: none)_


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| context | DatasetContext | Dataset Contextto use |
| record | Object | Record to take the image from |
| field | string | (mandatory)Field to use. |
| domainUrl | string | The base URL of the domain where the dataset can be found. By default, the current domain is used.(default: none) |

---
### odsResultEnumerator

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsResultEnumerator widget enumerates the search results (records for a Dataset Context, datasets for a Catalog Context). It repeats the template (the content of the directive element) for each of them.

If used with a Catalog Context, for each result, the following AngularJS variables are available:

  * `item.datasetid`: Dataset identifier of the dataset
  * `item.metas`: An object holding the key/values of metadata for this dataset



If used with a Dataset Context, for each result, the following AngularJS variables are available:

  * `item.datasetid`: Dataset identifier of the dataset this record belongs to
  * `item.fields`: an object hold all the key/values for the record
  * `item.geometry`: if the record contains geometrical information, this object is present and holds its GeoJSON representation




#### Usage

as element:
      
      1. <ods-result-enumerator
        2.        context="{CatalogContext|DatasetContext}"
        3.        max="{number}"
        4.        show-hits-counter="{boolean}"
        5.        show-pagination="{boolean}">
        6. </ods-result-enumerator>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
context| [CatalogContext]()[DatasetContext]()| Catalog Context or Dataset Context to use  
max| [number]()| Maximum number of results to show. The value can be changed dynamically using a variable. _(default: 10)_  
showHitsCounter| [boolean]()| Displays the number of hits (search results). This is the number of results available on the API, not the number of results displayed in the widget. _(default: false)_  
showPagination| [boolean]()| Displays a pagination block below the results to be able to browse them all. _(default: false)_


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| context | CatalogContextDatasetContext | Catalog ContextorDataset Contextto use |
| max | number | Maximum number of results to show. The value can be changed dynamically using a variable.(default: 10) |
| showHitsCounter | boolean | Displays the number of hits (search results). This is the number of results available on the API, not the number of results displayed in the widget.(default: false) |
| showPagination | boolean | Displays a pagination block below the results to be able to browse them all.(default: false) |

---
### odsResults

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsResults widget exposes the results of a search as an array in a variable available in the scope. It can be used with the AngularJS ngRepeat directive to build a list of results simply. It also adds to the context variable a `nhits` property containing the total number of records matching the query regardless of the odsResultsMax value.


#### Usage

as attribute
      
      1. <ANY ods-results="{string}"
        2.      ods-results-context="{CatalogContext|DatasetContext}"
        3.      ods-results-max="{number}">
        4.    ...
        5. </ANY>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
odsResults| [string]()| Variable name to use _(default: results)_  
odsResultsContext| [CatalogContext]()[DatasetContext]()| Catalog Context or Dataset Context to use  
odsResultsMax| [number]()| Maximum number of results to show. The value can be changed dynamically using a variable. _(default: 10)_


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| odsResults | string | Variable name to use(default: results) |
| odsResultsContext | CatalogContextDatasetContext | Catalog ContextorDataset Contextto use |
| odsResultsMax | number | Maximum number of results to show. The value can be changed dynamically using a variable.(default: 10) |

---
### odsReuses

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsReuses widget displays all reuses published on a domain in an infinite list of large boxes, presenting reuses in a clear display. The list shows the more recent reuses first.

You can optionally insert HTML code inside the `<ods-reuses></ods-reuses>` element, in which case it will be used as a template for each displayed reuse. The following variables are available in the template:

  * `reuse.url`: URL to the reuse's dataset page
  * `reuse.title`: Title of the reuse
  * `reuse.thumbnail`: URL to the thumbnail of the reuse
  * `reuse.description`: Description of the reuse
  * `reuse.created_at`: ISO datetime of reuse's original submission (can be used as `reuse.created_at|moment:'LLL'` to format it)
  * `reuse.dataset.title`: Title of the reuse's dataset
  * `reuse.user.last_name`: Last name of the reuse's submitter
  * `reuse.user.first_name`: First name of the reuse's submitter




#### Usage

as element:
      
      1. <ods-reuses
        2.        context="{CatalogContext}">
        3. </ods-reuses>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
context| [CatalogContext]()| Catalog Context to use


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| context | CatalogContext | Catalog Contextto use |

---
### odsSearchbox

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsSearchbox widget displays a wide search box that redirects the search on the Explore homepage of the domain.


#### Usage

as element:
      
      1. <ods-searchbox
        2.        placeholder="{string}"
        3.        sort="{string}"
        4.        context="{CatalogContext}"
        5.        [autofocus]="{string}"
        6.        form-id="{string}">
        7. </ods-searchbox>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
placeholder| [string]()| Controls the text to display as a placeholder when the search box is empty.  
sort| [string]()| Controls the default sort order for the results.  
context| [CatalogContext]()| Catalog Context indicating the domain to redirect the user to show the search results. If `none`, the search is performed on the local domain; that is, the domain to which the widget has been added. _(default: none)_  
[autofocus]| [string]()| Adds the autofocus attribute to set the focus in the text search input. No value is required.  
formId| [string]()| Configures the `id` attribute of the form generated internally by the widget, which can be used from other HTML elements. For example, it can be used to submit the search from another button. _(default: none)_


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| placeholder | string | Controls the text to display as a placeholder when the search box is empty. |
| sort | string | Controls the default sort order for the results. |
| context | CatalogContext | Catalog Contextindicating the domain to redirect the user to show the search results. Ifnone, the search is performed on the local domain; that is, the domain to which the widget has been added.(default: none) |
| [autofocus] | string | Adds the autofocus attribute to set the focus in the text search input. No value is required. |
| formId | string | Configures theidattribute of the form generated internally by the widget, which can be used from other HTML elements. For example, it can be used to submit the search from another button.(default: none) |

---
### odsSelect

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsSelect widget shows a list of options from which users can select one or more options. This list can be made up of strings or objects.

If the `options` variable provided to the widget represents a simple array of strings, option labels and values will be automatically calculated by the widget. If the options provided to the widget are objects, use the `label-modifier` and `value-modifier` parameters to define how to handle those objects.

The `label-modifier` and `value-modifier` parameters each take an expression applied to each object representing an option. Finally, the selection will be stored in the variable specified in the `selected-values` parameter.

### Explanation of the examples

#### First example

The first example shows a list of options from which users can select one or multiple trees. This example uses the `ods-dataset-context`, `ods-result`, and `ods-select` widgets:

  * The `ods-dataset-context` declares a context based on the `les-arbres-remarquables-de-paris` dataset.
  * The `ods-results` widget is nested within `ods-dataset-context`. It stores the result of the search request in the variable `items`. The value of the variable `items` will have this form:


      
      1. [
        2.     { fields: { libellefrancais: "Noyer", espece: "nigra",  ... }, ... },
        3.     { fields: { libellefrancais: "Marronnier", espece: "hippocastanum",  ... }, ... },
        4.     { fields: { libellefrancais: "Chêne", espece: "cerris",  ... }, ... },
        5.     ...
        6. ]
    
    

  * The `ods-select` widget is nested within `ods-results`. It defines the list of options users can select, using the `options` parameter set to `items`. `items` corresponds to the variable storing the results in `ods-results`.



**The parameter`label-modifier`**

In this example, the desired value for the option label is the field `libellefrancais` from the source dataset. To access the value of this field, the `label-modifier` parameter for `ods-select` is set to `"fields.libellefrancais"`.

**The parameter`value-modifier`**

The desired structure for the values returned by `selected-values` is the following:
      
      1. [
        2.     { name: "Noyer", species: "nigra" },
        3.     { name: "Marronnier", species: "hippocastanum" },
        4.     ...
        5. ]
    
    

To achieve this, the `value-modifier` for `ods-select` is set to `"{ 'name': fields.libellefrancais, 'species': fields.espece }"`.

#### Second example

The second example shows two lists of options from which users can select one or multiple options:

  * From the first list, users can select districts.
  * From the second list, users can select tree species.



In the second example, context parameters are updated by injecting the selected values returned by `ods-select`. This example uses the `ods-dataset-context`, `ods-result`, and `ods-select` widgets:

  * The `ods-dataset-context` declares a context based on the `les-arbres-remarquables-de-paris` dataset.
  * Two `ods-results` widgets are nested within `ods-dataset-context`. They fetch the values of the facets "arrondissement" and "libellefrancais" from the source dataset and store them in the variables `facetsArrondissement` and `facetsLibelleFrancais`, respectively. The values of `facetsArrondissement` and `facetsLibelleFrancais` will have this form:


      
      1. [
        2.     { count: 1, path: "PARIS 1ER ARRDT", state: "displayed", name: "PARIS 1ER ARRDT" },
        3.     { count: 8, path: "PARIS 17E ARRDT", state: "displayed", name: "PARIS 17E ARRDT" },
        4.     { count: 11, path: "PARIS 7E ARRDT", state: "displayed", name: "PARIS 7E ARRDT" },
        5.     ...
        6. ]
    
    
      
      1. [
        2.     { count: 32, path: "Platane", state: "displayed", name: "Platane" },
        3.     { count: 12, path: "Hêtre", state: "displayed", name: "Hêtre" },
        4.     { count: 11, path: "Chêne", state: "displayed", name: "Chêne" },
        5.     ...
        6. ]
    
    

  * An `ods-select` widget is nested within each `ods-results`. They define the lists of options users can select, using the `options` parameter set to `facetsArrondissement` and `facetsLibelleFrancais`, respectively. To update the context each time an option is selected, the `selected-values` parameters for `ods-select` are set to `ctx.parameters['refine.arrondissement']` and `ctx.parameters['refine.libellefrancais']`, respectively.




#### Usage

as element:
      
      1. <ods-select
        2.        options="{array}"
        3.        selected-values="{array}"
        4.        label-modifier="{expression}"
        5.        value-modifier="{expression}"
        6.        on-change="{expression}"
        7.        multiple
        8.        is-loading="{boolean}"
        9.        disabled
        10.        placeholder="{string}">
        11. </ods-select>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
options| [array]()| The input array of value which feeds the list of options  
selectedValues| [array]()| The variable name to use to store the selected options' values  
labelModifier| [expression]()| An expression to apply on the options' label _(default: none)_  
valueModifier| [expression]()| An expression to apply on the options' value. This parameter is used to modify the form of the values exposed by `selected-value`. _(default: none)_  
onChange| [expression]()| An expression to evaluate whenever an option has been (de)selected _(default: none)_  
multiple| [boolean]()| When set to `true`, the menu will support multiple selections. _(default: false)_  
isLoading| [boolean]()| Specifies whether the widget should initially display a loader. This parameter will be automatically set to `false` as soon as options are loaded. _(default: false)_  
disabled| [boolean]()| Specifies whether the widget should be disabled. _(default: false)_  
placeholder| [string]()| Specifies a short hint that describes the expected value of the select field. _(default: "Select one or more elements" or "Select one element")_


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| options | array | The input array of value which feeds the list of options |
| selectedValues | array | The variable name to use to store the selected options' values |
| labelModifier | expression | An expression to apply on the options' label(default: none) |
| valueModifier | expression | An expression to apply on the options' value. This parameter is used to modify the form of the values exposed byselected-value.(default: none) |
| onChange | expression | An expression to evaluate whenever an option has been (de)selected(default: none) |
| multiple | boolean | When set totrue, the menu will support multiple selections.(default: false) |
| isLoading | boolean | Specifies whether the widget should initially display a loader. This parameter will be automatically set tofalseas soon as options are loaded.(default: false) |
| disabled | boolean | Specifies whether the widget should be disabled.(default: false) |
| placeholder | string | Specifies a short hint that describes the expected value of the select field.(default: "Select one or more elements" or "Select one element") |

---
### odsSimpleTab

**Module:** `ods-widgets`
**Type:** Directive


#### Usage

as element:
      
      1. <ods-simple-tab
        2.        label="{string}"
        3.        fontawesome-class="{string}"
        4.        keep-content="{boolean}">
        5. </ods-simple-tab>
    
    

#### Parameters

Param| Type| Details  
---|---|---  
label| [string]()| The label to be displayed in the tab  
fontawesomeClass| [string]()| The Font Awesome icon name used for the tab, without the 'fa-' prefix  
keepContent| [boolean]()| By default, the widget destroys and rebuilds the pane content at deselection/selection. It acts like an ng-if when the panel is selected/deselected. When set to `true`, the widget does not destroy and rebuild the pane content at deselection/selection. _(default: false)_


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| label | string | The label to be displayed in the tab |
| fontawesomeClass | string | The Font Awesome icon name used for the tab, without the 'fa-' prefix |
| keepContent | boolean | By default, the widget destroys and rebuilds the pane content at deselection/selection. It acts like an ng-if when the panel is selected/deselected.When set totrue, the widget does not destroy and rebuild the pane content at deselection/selection.(default: false) |

---
### odsSimpleTabs

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsSimpleTabs widget generates a tabbed interface that allows you to switch between separate views.


#### Usage

as element:
      
      1. <ods-simple-tabs
        2.        sync-to-scope="{string}">
        3. </ods-simple-tabs>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
syncToScope| [string]()| Name of parent scope variable to sync the current active tab _(default: 'simpleTabActive')_


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| syncToScope | string | Name of parent scope variable to sync the current active tab(default: 'simpleTabActive') |

---
### odsSlideshow

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsSlideshow widget displays an image slideshow of a dataset containing media with thumbnails (images, PDF files, etc.).

You will need to set a height for the `.ods-slideshow` class to work correctly or set the height through the style attribute. You can also include a tooltip to access the image's record through the `record` variable.


#### Usage

as element:
      
      1. <ods-slideshow
        2.        context="{DatasetContext}"
        3.        image-field="{string}"
        4.        [title-fields]="{string}"
        5.        [domain-url]="{string}">
        6. </ods-slideshow>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
context| [DatasetContext]()| Dataset Context to use  
imageField| [string]()| The name of the field containing the image  
[titleFields]| [string]()| A comma-separated list of field names to display as comma-separated values in the title  
[domainUrl]| [string]()| The URL of the domain


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| context | DatasetContext | Dataset Contextto use |
| imageField | string | The name of the field containing the image |
| [titleFields] | string | A comma-separated list of field names to display as comma-separated values in the title |
| [domainUrl] | string | The URL of the domain |

---
### odsSocialButtons

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsSocialButtons widget displays a series of buttons for easy sharing on social media.


#### Usage

as attribute
      
      1. <ANY ods-social-buttons
        2.      buttons="{string}"
        3.      title="{string}"
        4.      url="{string}">
        5.    ...
        6. </ANY>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
buttons| [string]()| A comma-separated list of buttons you want to display _(default: 'twitter,facebook,linkedin,email')_  
title| [string]()| Title of the post on social media _(default: current page's title)_  
url| [string]()| URL attached to the post on social media _(default: current page's url)_


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| buttons | string | A comma-separated list of buttons you want to display(default: 'twitter,facebook,linkedin,email') |
| title | string | Title of the post on social media(default: current page's title) |
| url | string | URL attached to the post on social media(default: current page's url) |

---
### odsSpinner

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsSpinner widget displays the custom Opendatasoft spinner. Its size and color match the current font. If the browser doesn't support SVG animation via CSS, an animated GIF will be displayed instead.


#### Usage

as element:
      
      1. <ods-spinner>
        2. </ods-spinner>
    
    

### Directive info

  * This directive creates new scope.




---
### odsSubaggregation

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsSubaggregation widget computes aggregations on an analysis result. You can use this widget with the AngularJS ngRepeat directive to simply build a table of analysis results.


#### Usage

as attribute
      
      1. <ANY ods-subaggregation="{string}"
        2.      ods-subaggregation-serie*="{number}">
        3.    ...
        4. </ANY>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
odsSubaggregation| [string]()| Analysis results  
odsSubaggregationSerie*| [number]()| Aggregation expression


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| odsSubaggregation | string | Analysis results |
| odsSubaggregationSerie* | number | Aggregation expression |

---
### odsTable

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsTable widget displays a table view of a dataset, with infinite scroll and an ability to sort columns depending on the column types.


#### Usage

as element:
      
      1. <ods-table
        2.        context="{DatasetContext}"
        3.        displayed-fields="{string}">
        4. </ods-table>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
context| [DatasetContext]()| Dataset Context to use  
displayedFields| [string]()| A comma-separated list of fields to display. By default, all the available fields are displayed. _(default: all)_


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| context | DatasetContext | Dataset Contextto use |
| displayedFields | string | A comma-separated list of fields to display. By default, all the available fields are displayed.(default: all) |

---
### odsTagCloud

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsTagCloud widget displays a "tag cloud" of the values available in a facet. This facet can be the facet of a dataset or a facet from the dataset catalog. The "weight" (size) of a tag depends on the number of occurrences (count) for this tag.


#### Usage

as element:
      
      1. <ods-tag-cloud
        2.        context="{CatalogContext|DatasetContext}"
        3.        facet-name="{string}"
        4.        max="{number}"
        5.        redirect-to="{string}"
        6.        context-to-refine="{CatalogContext|DatasetContext}">
        7. </ods-tag-cloud>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
context| [CatalogContext]()[DatasetContext]()| Catalog Context or Dataset Context to use  
facetName| [string]()| Name of the facet to build the tag cloud from  
max| [number]()| Maximum number of tags to show in the cloud _(default: all)_  
redirectTo| [string]()| URL. If specified, a click on any tag will redirect to the given URL and apply the filter there. _(default: none)_  
contextToRefine| [CatalogContext]()[DatasetContext]()| Specifies the context that will be refined. If not specified at all, the refined context will be the one defined through the `context` parameter. _(default: current context)_


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| context | CatalogContextDatasetContext | Catalog ContextorDataset Contextto use |
| facetName | string | Name of the facet to build the tag cloud from |
| max | number | Maximum number of tags to show in the cloud(default: all) |
| redirectTo | string | URL. If specified, a click on any tag will redirect to the given URL and apply the filter there.(default: none) |
| contextToRefine | CatalogContextDatasetContext | Specifies the context that will be refined. If not specified at all, the refined context will be the one defined through thecontextparameter.(default: current context) |

---
### odsTextSearch

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsTextSearch widget displays a search box to perform a full-text search in a context.


#### Usage

as element:
      
      1. <ods-text-search
        2.        context="{CatalogContext|DatasetContext|CatalogContext[]|DatasetContext[]}"
        3.        placeholder="{string}"
        4.        field="{string}"
        5.        suffix="{string}"
        6.        autofocus="{string}"
        7.        id="{string}">
        8. </ods-text-search>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
context| [CatalogContext]()[DatasetContext]()[CatalogContext[]]()[DatasetContext[]]()| _(mandatory)_ Catalog Context, Dataset Context, or array of context to use  
placeholder| [string]()| Text to display as a placeholder when the search box is empty _(default: none)_  
field| [string]()| Name of a field the search will be restricted on (i.e., the widget will only allow to search on the textual content of the chosen field). If more than one context is declared, it is possible to specify different fields depending on these contexts, using the following syntax: mycontext-field. If a specific field is not set for a context, the value of the field parameter will be used by default. The search will be a simple text search that won't support query languages and operators. _(default: none)_  
suffix| [string]()| Changes the default `q` query parameter into `q.suffixValue`. This parameter prevents widgets from overriding one another, for instance when multiple odsTextSearch widgets are used on the same page. _(default: none)_  
autofocus| [string]()| Makes the search box automatically selected at loading of the page to start typing the search without selecting the search box manually beforehand. No value is required for this parameter to function.  
id| [string]()| Adds an `id` attribute to the search's text box, for example, to integrate the widget to a clickable label.


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| context | CatalogContextDatasetContextCatalogContext[]DatasetContext[] | (mandatory)Catalog Context,Dataset Context, or array of context to use |
| placeholder | string | Text to display as a placeholder when the search box is empty(default: none) |
| field | string | Name of a field the search will be restricted on (i.e., the widget will only allow to search on the textual content of the chosen field). If more than one context is declared, it is possible to specify different fields depending on these contexts, using the following syntax: mycontext-field. If a specific field is not set for a context, the value of the field parameter will be used by default. The search will be a simple text search that won't support query languages and operators.(default: none) |
| suffix | string | Changes the defaultqquery parameter intoq.suffixValue. This parameter prevents widgets from overriding one another, for instance when multiple odsTextSearch widgets are used on the same page.(default: none) |
| autofocus | string | Makes the search box automatically selected at loading of the page to start typing the search without selecting the search box manually beforehand. No value is required for this parameter to function. |
| id | string | Adds anidattribute to the search's text box, for example, to integrate the widget to a clickable label. |

---
### odsThemeBoxes

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsThemeBoxes widget enumerates the themes available on the domain by showing their pictograms and the number of datasets they contain. They require the `themes` setting to be configured in ODSWidgetsConfig.


#### Usage

as element:
      
      1. <ods-theme-boxes
        2.        context="{CatalogContext}">
        3. </ods-theme-boxes>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
context| [CatalogContext]()| Catalog Context to pull the theme list from


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| context | CatalogContext | Catalog Contextto pull the theme list from |

---
### odsThemePicto

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsThemePicto widget displays the pictogram of a theme based on the `themes` setting in ODSWidgetsConfig. This element can be styled (height, width, etc.), especially if the pictogram is vectorial (SVG).


#### Usage

as element:
      
      1. <ods-theme-picto
        2.        theme="{string}">
        3. </ods-theme-picto>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
theme| [string]()| The label of the theme to display the pictogram of


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| theme | string | The label of the theme to display the pictogram of |

---
### odsTimer

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsTimer widget is a simple timer. It executes the AngularJS expression `exec` every `delay` milliseconds. It doesn't stop until the user clicks on the pause button or when the `stopCondition` is true.

It can be used to animate dashboards to go over a date field and add one day every two seconds, like in the following example. "From" and "To" values will increase by one day until the user clicks on the pause button.


#### Usage

as element:
      
      1. <ods-timer
        2.        delay="{Number}"
        3.        stop-condition="{Expression}"
        4.        auto-start="{Boolean}"
        5.        [exec]="{Expression}">
        6. </ods-timer>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
delay| [Number]()| The number of milliseconds to wait before executing the expression. The minimum value is `100`. _(default: 1000)_  
stopCondition| [Expression]()| An AngularJS expression returning 'true' or 'false'. The timer stops when the condition is 'false'. _(default: false)_  
autoStart| [Boolean]()| Starts the timer automatically when the page loads. _(default: false)_  
[exec]| [Expression]()| An AngularJS expression to execute.


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| delay | Number | The number of milliseconds to wait before executing the expression. The minimum value is100.(default: 1000) |
| stopCondition | Expression | An AngularJS expression returning 'true' or 'false'. The timer stops when the condition is 'false'.(default: false) |
| autoStart | Boolean | Starts the timer automatically when the page loads.(default: false) |
| [exec] | Expression | An AngularJS expression to execute. |

---
### odsTimerange

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsTimerange widget displays two fields to select the two bounds of a date and time range.

The values for the `defaultTo` and `defaultFrom` parameters MUST be in `YYYY-MM-DD HH:mm` (or `YYYY-MM-DD` for date only) whatever the displayFormat.


#### Usage

as element:
      
      1. <ods-timerange
        2.        context="{DatasetContext|DatasetContext[]}"
        3.        [time-field="{string}"]
        4.        [{context}-time-field="{string}"]
        5.        default-from="{string}"
        6.        default-to="{string}"
        7.        display-time="{string}"
        8.        date-format="{string}"
        9.        suffix="{string}"
        10.        label-from="{string}"
        11.        label-to="{string}"
        12.        placeholder-from="{string}"
        13.        placeholder-to="{string}"
        14.        to="{string}"
        15.        from="{string}">
        16. </ods-timerange>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
context| [DatasetContext]()[DatasetContext[]]()| Dataset Context or array of context to use  
timeField _(optional)_| [string]()| The value is the name of the field (date or datetime) to filter on.  
  
_Use this form if you apply the timerange to only one context._ _(default: first date/datetime field available)_  
{context}TimeField _(optional)_| [string]()| The value is the name of the field (date or datetime) to filter on.  
  
_Use this form when you apply the timerange to multiple contexts. {context} must be replaced by the context name._ _(default: first date/datetime field available)_  
defaultFrom| [string]()| Default datetime for the "from" field: either "yesterday", "now" or a string representing a date. This value always uses the `YYYY-MM-DD HH:mm` or `YYYY-MM-DD` format. _(default: none)_  
defaultTo| [string]()| Default datetime for the "to" field: either "yesterday", "now", or a string representing a date. This value always uses the `YYYY-MM-DD HH:mm` or `YYYY-MM-DD` format. _(default: none)_  
displayTime| [string]()| Defines if the date selector displays the time selector as well _(default: true)_  
dateFormat| [string]()| Defines the format for the date displayed in the inputs _(default: 'YYYY-MM-DD HH:mm')_  
suffix| [string]()| (optional) Adds a suffix to the q.timerange, q.from_date or q.to_date parameter. This prevents widgets from overriding each other. _(default: 'fieldname')_  
labelFrom| [string]()| Sets the label before the first input _(default: 'From')_  
labelTo| [string]()| Sets the label before the second input _(default: 'to')_  
placeholderFrom| [string]()| Sets the label before the first input _(default: '')_  
placeholderTo| [string]()| Sets the label before the second input _(default: '')_  
to| [string]()| Sets a variable that will get the iso formatted value of the first input _(default: none)_  
from| [string]()| Sets a variable that will get the iso formatted value of the second input _(default: none)_


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| context | DatasetContextDatasetContext[] | Dataset Contextor array of context to use |
| timeField(optional) | string | The value is the name of the field (date or datetime) to filter on.Use this form if you apply the timerange to only one context.(default: first date/datetime field available) |
| {context}TimeField(optional) | string | The value is the name of the field (date or datetime) to filter on.Use this form when you apply the timerange to multiple contexts. {context} must be replaced by the context name.(default: first date/datetime field available) |
| defaultFrom | string | Default datetime for the "from" field: either "yesterday", "now" or a string representing a date. This value always uses theYYYY-MM-DD HH:mmorYYYY-MM-DDformat.(default: none) |
| defaultTo | string | Default datetime for the "to" field: either "yesterday", "now", or a string representing a date. This value always uses theYYYY-MM-DD HH:mmorYYYY-MM-DDformat.(default: none) |
| displayTime | string | Defines if the date selector displays the time selector as well(default: true) |
| dateFormat | string | Defines the format for the date displayed in the inputs(default: 'YYYY-MM-DD HH:mm') |
| suffix | string | (optional) Adds a suffix to the q.timerange, q.from_date or q.to_date parameter. This prevents widgets from overriding each other.(default: 'fieldname') |
| labelFrom | string | Sets the label before the first input(default: 'From') |
| labelTo | string | Sets the label before the second input(default: 'to') |
| placeholderFrom | string | Sets the label before the first input(default: '') |
| placeholderTo | string | Sets the label before the second input(default: '') |
| to | string | Sets a variable that will get the iso formatted value of the first input(default: none) |
| from | string | Sets a variable that will get the iso formatted value of the second input(default: none) |

---
### odsTimescale

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsTimescale widget displays a control to select:

  * the last day,
  * the last week,
  * the last month, or
  * the last year.




#### Usage

as element:
      
      1. <ods-timescale
        2.        context="{DatasetContext|DatasetContext[]}"
        3.        [time-field="{string}"]
        4.        [*-time-field="{string}"]
        5.        [default-value="{string}"]>
        6. </ods-timescale>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
context| [DatasetContext]()[DatasetContext[]]()| Dataset Context or array of context to use  
timeField _(optional)_| [string]()| Name of the field (date or datetime) to filter on _(default: first date/datetime field available)_  
*TimeField _(optional)_| [string]()| For each context, you can set the name of the field (date or datetime) to filter on. _(default: first date/datetime field available)_  
defaultValue _(optional)_| [string]()| Sets the default timescale. _(default: everything)_


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| context | DatasetContextDatasetContext[] | Dataset Contextor array of context to use |
| timeField(optional) | string | Name of the field (date or datetime) to filter on(default: first date/datetime field available) |
| *TimeField(optional) | string | For each context, you can set the name of the field (date or datetime) to filter on.(default: first date/datetime field available) |
| defaultValue(optional) | string | Sets the default timescale.(default: everything) |

---
### odsToggleModel

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsToggleModel widget, when used on a checkbox, allows the checkbox to be used to "toggle" a value in an object. In other words, the value is added when the checkbox is selected and removed when the checkbox is cleared.

Multiple checkboxes can be used on the same model and key, in which case if two or more are toggled, an array will be created to hold the values.


#### Usage

as attribute
      
      1. <ANY ods-toggle-model="{Object}"
        2.      ods-toggle-key="{string}"
        3.      ods-toggle-value="{string}"
        4.      ods-store-as="{string}">
        5.    ...
        6. </ANY>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
odsToggleModel| [Object]()| Object to apply the toggle on  
odsToggleKey| [string]()| The key holding the toggled value  
odsToggleValue| [string]()| The toggled value  
odsStoreAs| [string]()| The type of the resulting variable. The authorized values are 'array' and 'csv'. _(default: array)_


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| odsToggleModel | Object | Object to apply the toggle on |
| odsToggleKey | string | The key holding the toggled value |
| odsToggleValue | string | The toggled value |
| odsStoreAs | string | The type of the resulting variable. The authorized values are 'array' and 'csv'.(default: array) |

---
### odsTopPublishers

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsTopPublishers widget displays the five top publishers.


#### Usage

as element:
      
      1. <ods-top-publishers
        2.        context="{CatalogContext}">
        3. </ods-top-publishers>
    
    

### Directive info

  * This directive creates new scope.



#### Parameters

Param| Type| Details  
---|---|---  
context| [CatalogContext]()| Catalog Context to use


#### Parameters

| Parameter | Type | Details |
|-----------|------|---------|
| context | CatalogContext | Catalog Contextto use |

---
### odsWidgetTooltip

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The odsWidgetTooltip widget is a helper for displaying custom tooltips.

It allows to configure the usable fields in the tooltip and the template and does the HTML rendering giving back the compiled HTML to the calling widget.

By default, the template for the custom tooltip can access the record and a displayedFields array that lists the record fields that should appear in the tooltip.


#### Usage

as attribute
      
      1. <ANY ods-widget-tooltip>
        2.    ...
        3. </ANY>
    
    


---
### refineOnClick

**Module:** `ods-widgets`
**Type:** Directive

#### Description

The refineOnClick directive will refine the given context(s) for a click on an element representing a record.

It works in conjunction with a finite set of other directives:

  * odsCalendar
  * odsMediaGallery
  * odsMap
  * odsChart
  * odsChartSerie



When clicking on an item, the contexts will be refined using the values in the configured fields. By default, if you click on more than one item, the refinements will add up, which can be useful in situations with multiples values. If you prefer the refinement to be replaced each time you click, you can use `refineOnClickReplaceRefine`.


#### Usage

as attribute
      
      1. <ANY refine-on-click>
        2.    ...
        3. </ANY>
    
    

### Directive info

  * This directive creates new scope.




---
