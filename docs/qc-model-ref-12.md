# Template for Quality Models

Reviewer: VL (Violaine Louvet)

Reference: (ID = 146) - Quantitative evaluation of software quality, Boehm B.W., Brown J.R., Lipow M. https://www.scopus.com/inward/record.uri?eid=2-s2.0-85042377749&partnerID=40&md5=86df793c94725cf352a0b8b3d8227c3c

| Codename | Name  | Definition | Aut(omate)/Man(ual) | Category | Comment |
| :------: | :---: | :--------: | :-----------------: | :------: | :-----: |
| | ACCESSIBILITY | facilitates selective use of its parts. | man | technical accessibility | Necessary for efficiency, testability and human engineering |
| | ACCOUNTABILITY | its usage can be measured; critical segments of code can be instrumented with probes to measure timing, whether specified branches are  exercised, etc. | aut |          Performance, Resource utilization          | |
| | ACCURACY | its outputs are sufficiently precise to satisfy their intended us | aut | Performance | Necessary for reliability |
| | AUGMENTABILITY | it can easily accommodate expansion in component computational functions or data storage requirements | man | interoperability, modifiability | Necessary for modifiability |
| | COMMUNICATIVENESS | it  facilitates the specification of inputs and provides outputs whose form and content are easy to assimilate and useful. | man ? | Ease of use, supportability | Necessary for testability and human engineering |
| | COMPLETENESS | all its parts are present and each part is fully developed. | man | Documentation, manageability | External references are available and required functions are coded and present as designe |
| | CONCISENESS | excessive information is not present. | man | Documentation, resource utilization | Programs are not excessively fragmented nor the same sequence of code is repeated in numerous place ... |
| | CONSISTENCY | it contains uniform notation, terminology and symbology within itself | aut ? | Interoperability, compatibility | Coding standards are homogeneously adhered to |
| | DEVICE-INDEPENDENCE | it can be executed on computer hardware configurations other than its current on | aut | Portability | Necessary for portability |
| | EFFICIENCY | it fulfills its purpose without waste of resources. | aut |          Performance, resource utilization          | Choice of efficient algorithm ... |
| | HUMAN ENGINEERING | it fulfills its purpose without wasting the users' time and energy, or degrading their morale | man | Ease of use | Implies accessibility, robustness and communicativeness |
| | LEGIBILITY | its function is easily discerned by reading the code | man | Documentation, ease of use | Necessary for understandability |
| | MAINTAINABILITY | it facilitates updating to satisfy new requirements or to correct deficiencies. | man | Maintainability | Code understandable, testable and modifiable |
| | MODIFIABILITY | it facilitates the incorporation of changes, once the nature of the desired change has been determined | man | Modifiability | |
| | PORTABILITY | it can be operated easily and well on computer configurations other than its current one. | aut | Portability | Use of standard library function ... |
| | RELIABILITY | it can be expected to perform it s intended functions satisfactorily | aut | Reliability, installability | The program will compile, load and execute, producing answers of the requisite accuracy |
| | ROBUSTNESS | it can continue to perform despite some violation of the assumptions in its specification | man | Safety | The program will properly handle inputs out of range or in different format ... |
| | SELF-CONTAINEDNESS | it performs all its explicit and implicit functions within itself . | aut ? | ?? | Example of implicit functions : initialization, input checking ... |
| | SELF-DESCRIPTIVENESS | it contains enough information for a reader to determine or verify its  objectives, assumptions, constraints, inputs, outputs, components, and  revision status. | man | Documentation, ease of use | Necessary for testability and understandability |
| | STRUCTUREDNESS | it possesses a definite pattern of organization of its interdependent parts. | man | Modifiability, reusability | Standard control structure have been followed in coding |
| | TESTABILITY | it facilitates the establishment of verification criteria and supports evaluation of its performance. | aut | Testability | requirements are match to specific modules or diagnostics capabilities are provided |
| | UNDERSTANDABILITY | its purpose is clear to the inspector. | man | Documentation, ease of use, technical accessibility | Names are used consistently, modules are self-descriptive, ... |
| | USABILITY (AS-lS UTILITY) | it is reliable, efficient and human-engineered. | man | Ease of use, Performance | The function performed by the program is useful elsewhere, is robust  against human errors or does not require excessive core memory... |

* Note : old paper (1976 !) but founding article for the Boehm model
