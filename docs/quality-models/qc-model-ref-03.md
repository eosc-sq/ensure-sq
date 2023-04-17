# QM Reference 03: (paper ID = 45)

Reviewer: JC (Leyla Jael Castro)

A systematic review of quality attributes and measures for software product lines
Montagud S., Abrahão S., Insfran E.
<https://www.scopus.com/inward/record.uri?eid=2-s2.0-84865626740&doi=10.1007%2fs11219-011-9146-7&partnerID=40&md5=33b25cd0a25fc09685e06cbc9c988f14>


| Codename | Name | Definition | Aut(omate)/Man(ual) | Characteristics | Comment |
| :------: | :---: | :--------: | :-----------------: | :-------------: | :-----: |
| BSize | Binary size | Binary size | Aut | Maintainability | Value. Quantitativ. Direct. Binary size can be calculated for the whole software or for modules/components/classes. |
| NumMod | Number of modules | Number of modules/components/classes | Aut | Maintainability | Value. Quantitative. Direct for classes, (un)direct depending on how modules/components are defined. Number of modules/components/classes. On its own does not say much but could be used for complexity or bug metrics. |
| NumLines | Number of lines | Number of lines for the whole software or components/modules/classes/functions/methods | Aut | Maintainability | Value. Quantitative. Direct for classes, (un)direct depending on how modules/components are defined. Number of lines can be counted for the whole software or for modules/components/classes or even methods/functions. On its own does not say much but could be used for complexity metrics. |
| NumComLines | Number of comments | Number of lines corresponding to comments for the whole software or per modules/components/classes/functions/methods | Aut | Maintainability. Reusability | Value. Quantitative. Direct for classes, (un)direct depending on how modules/components are defined.. On its own does not say much but could be used for documentation metrics (e.g. ratio of inline documentation). |
| CyComSC | Complexity of the source code | Cyclomatic complexity or the whole software or modules/components/classes/functions/methods. Number of linearly independent paths through a program's source code. Source https://docs.microsoft.com/en-us/visualstudio/code-quality/code-metrics-values?view=vs-2022: Measures the structural complexity of the code. It is created by calculating the number of different code paths in the flow of the program. A program that has complex control flow requires more tests to achieve good code coverage and is less maintainable. | Aut | Maintainability | Metric. Quantitative. Could require external app to measure it |
| ComDiag | Complexity of diagrams for the whole software or modules/components | | Man | Maintainability. Reusability | Metric. Qualitative (was Quantitative in the article). Requires well established software engineering practices. Alternative: Software diagram Yes/No |
| ComArc | Complexity of an architecture | | Man | Maintainability. Reusability | Metric. Qualitative (was Quantitative in the article). Requires well established software engineering practices. Alternative: Architecture diagram Yes/No |
| ComUC | Complexity of a use case | | Man | Maintainability. Reusability. Usability | Metric. Qualitative (was Quantitative in the article). Requires well established software engineering practices. Alternative: Use case Yes/No |
| ComUCDi | Complexity of a use case diagram | | Man | Maintainability. Reusability. Usability | Metric. Qualitative (was Quantitative in the article). Alternative: Use cases diagram Yes/No |
| MI | Maintainability Index (MI) for the whole, for a module/component, for the architecture | Source https://docs.microsoft.com/en-us/visualstudio/code-quality/code-metrics-values?view=vs-2022: Calculates an index value between 0 and 100 that represents the relative ease of maintaining the code. A high value means better maintainability. Color coded ratings can be used to quickly identify trouble spots in your code. A green rating is between 20 and 100 and indicates that the code has good maintainability. A yellow rating is between 10 and 19 and indicates that the code is moderately maintainable. A red rating is a rating between 0 and 9 and indicates low maintainability | Aut | Maintainability | Metric. Quantitative |
| EffCh | Effort required for changes | Time and resources dedicated to resolve an issue | Aut/Man | Reliability | Value. Quantitative/Qualitative. Useful to calculate maturity |
| Mat | Maturity | Time for the code to fail, number of resolved bugs, number of open bugs | Aut/Man | Reliability | Metric. Quantitative |
| Cop | Coupling | Source https://docs.microsoft.com/en-us/visualstudio/code-quality/code-metrics-values?view=vs-2022: Measures the coupling to unique classes through parameters, local variables, return types, method calls, generic or template instantiations, base classes, interface implementations, fields defined on external types, and attribute decoration. Good software design dictates that types and methods should have high cohesion and low coupling. High coupling indicates a design that is difficult to reuse and maintain because of its many interdependencies on other types. Source https://en.wikipedia.org/wiki/Coupling_(computer_programming): Coupling refers to the interdependencies between modules | Aut | Maintainability | Metric. Quantitative (could require additional app for calculation) |
| Coh | Internal cohesion | Source https://en.wikipedia.org/wiki/Coupling_(computer_programming): Cohesion describes how related the functions within a single module are. Low cohesion implies that a given module performs tasks which are not very related to each other and hence can create problems as the module becomes large | Aut | Maintainability | Metric. Quantitative (could require additional app for calculation) |