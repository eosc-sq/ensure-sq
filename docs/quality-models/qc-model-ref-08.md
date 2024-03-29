# QM Reference 08: (paper ID = 128)

Reviewer: MC (Miguel Colom)

Experiences of software quality management using metrics through the life-cycle, Ogasawara Hideto, Yamada Atsushi, Kojo Michiko
<https://www.scopus.com/inward/record.uri?eid=2-s2.0-0029516009&partnerID=40&md5=68106def0b53f2f1a609753364cb4705>

| Codename | Name  | Definition | Aut(omate)/Man(ual) | Characteristics | Comment |
| :------: | :---: | :--------: | :-----------------: | :------: | :-----: |
||Number of Modules|number of software components the complete source has|Aut|Maintainability||
||Number of Steps|number of function calls|Aut|Maintainability|a "step" is a call to a function in the terminology of this article.|
||Number of Include Files|number of imported modules|Aut|Maintainability|this includes the modules of the program and external libraries|
||Number of Conditions|number of condition checks to perform an operation|Aut|Maintainability|for example, conditions in "if" or "while" loops|
||Number of Loops|number of loops in the program|Aut|Maintainability|similar to "Number of Conditions", but specific to loops|
||Number of Arguments|number of arguments in the functions|Aut|Maintainability||
||Number of Comments|number of comments in the source code|Aut|Modifiability||

Note: I'm adding "Modifiability" for the last row, but it's more related to documentation. However, we don't have anything related to the quality of documentation in out list of Software Quality Characteristics.
