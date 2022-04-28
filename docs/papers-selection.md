# Proposed template (for each paper to review):

Table columns of template:

* Paper_id: paper id in the list below, for example ID = 11 for the first paper.
* Name: name of criteria.
* Definition: description/summary of the criteria.
* Qualitative/quantitative: if the criteria is objective/measurable (possible to automate) or subjective and difficult to automate.
* Targeted to SW (see <https://github.com/eosc-sq/overleaf-ensure-sq/blob/main/landscaping.tex>): at the, moment one of:
  * Library
  * Framework
  * Application (such as Monte-Carlo simulation)
  * Analysis script
  * Services and platforms
* Reviewer(s): reviewer short name, for example DG for Daniel Garijo, see below.
* Comment: any other comment the reviewer sees fit to make.

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
|          |       |            |                          |                |           |         |

## Reviewers

* DG - Daniel Garijo
* ER - Elisabetta Ronchieri
* JC - Leyla Jael Castro
* LC - Laura del Cano
* MC - Miguel Colom
* MD - Mario David
* MT - Massimo Torquati
* MV - Maxime Van den Bossche
* VL - Violaine Louvet
* IC - Isabel Campos

# Selected with **yes** and **yes + unsure** - Total 29 articles

---

## 11 - Software quality through the eyes of the end-user and static analysis tools: A study on Android OSS applications

### Srisopha K., Alfayez R.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-85051522416&doi=10.1145%2f3194095.3194096&partnerID=40&md5=7a9dc5d4116e134e2a85128cb3328d90

Source code analysis tools have been the vehicle for measuring and assessing the quality of a software product for decades. However, recently many studies have shown that post-deployment end-user reviews provide a wealth of insight into the quality of a software product and how it should evolve and be maintained. For example, end-user reviews help to identify missing features or inform developers about incorrect or unexpected software behavior. We believe that analyzing end-user reviews and utilizing analysis tools are a crucial step towards understanding the complete picture of the quality of a software product, as well as towards reasoning about the evolution history of it. In this paper, we investigate whether both methods correlate with one another. In other words, we explore if there exists a relationship between user satisfaction and the application's internal quality characteristics. To conduct our research, we analyze a total of 46 actual releases of three Android open source software (OSS) applications on the Google Play Store. For each release, we employ multiple static analysis tools to assess several aspects of the application's software quality. We retrieve and manually analyze the complete reviews after each release of each application from its store page, totaling 1004 reviews. Our initial results suggest that having high or low code quality does not necessary ensure user overall satisfaction. © 2018 Association for Computing Machinery.

| MD  | ER     | MC  | VL  | DG  | JC  | MV  |
| --- | ------ | --- | --- | --- | --- | --- |
|     | unsure |     | yes | yes | yes | yes |

* *ER* - this paper should be more related to the software development process.
* *JC* - Could include quality indicators based on end-user dimension
* *MV* - The end-user-review aspect could indeed be interesting.

### Review

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
| 11       | Code complexity      |  Paper does not provide a definition, but the less complex the code is, the better          |  Quantitative  | all types | DG        | See below    |
| 11       | Number of code smells      |  certain structures in the code which indicate a violation of fundamental design principles. The lower code smells, the better. Ref: Martin Fowler and Kent Beck. 1999. Refactoring: improving the design of existing code. Addison-Wesley Professional.  | Quanticative | all types | DG        | See below    |
| 11       | Comment density      | The idea here is that better commented code is easier to understand | Quantitative  | all types | DG        | See below    |
| 11       | User reviews      | The paper attempts to find correlation between user reviews and code quality. However, "to some extent, having high or low code quality does not necessary ensure user satisfaction" | Quantitative | apps with a store | DG        | See below    |
| 11       | PMD quality metrics     | Empty code, Naming, Braces, Import statements, Coupling, Unused Code, Unnecessary, Design, Optimization, String and StringBuffer | Quantitative | apps with a store | DG        | See below    |
| 11       | Findbugs quality metrics      | Dodgy code, Bad practice, Malicious code, Performance, Correctness, Security, Multithreaded correctness, Internalization | Quantitative | apps with a store | DG        | See below    |

**Comment**

This paper proposes a quality analysis from an empirical point of view. It uses three tools for quantitative analysis: SonarQube, PMD and FindBugs. The quality metrics are not proposed per se in the paper, but are useful candidates.

The paper mentions ISO/IEC 25010 software product quality characteristics. These are: .
  - functional suitability
  - performance efficiency
  - usability
  - portability
  - compatibility
  - reliability
  - maintainability
  - security

The following table shows how each tool tackles different metrics. However, some are not defined:

|Abbr.| Tool| Metric|
|:---:|:---:|:---:|
|CS| SonarQube| Number of code smells|
|PD| PMD| Empty code, Naming, Braces, Import statements, Coupling, Unused Code, Unnecessary, Design, Optimization, String and StringBuffer|
|FB| FindBugs| Dodgy code, Bad practice, Malicious code, Performance, Correctness, Security, Multithreaded correctness, Internalization|

---

## 41 - Fostering software quality assessment

### Brandtner M.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-84886382849&doi=10.1109%2fICSE.2013.6606725&partnerID=40&md5=9e042076903be6351b3b97be6a877cb3

Software quality assessment shall monitor and guide the evolution of a system based on quality measurements. This continuous process should ideally involve multiple stakeholders and provide adequate information for each of them to use. We want to support an effective selection of quality measurements based on the type of software and individual information needs of the involved stakeholders. We propose an approach that brings together quality measurements and individual information needs for a context-sensitive tailoring of information related to a software quality assessment. We address the following research question: How can we better support different stakeholders in the quality assessment of a software system? For that we will devise theories, models, and prototypes to capture their individual information needs, tailor information from software repositories to these needs, and enable a contextual analysis of the quality aspects. Such a context-sensitive tailoring will provide a effective and individual view on the latest development trends in a project. We outline the milestones as well as evaluation approaches in this paper. © 2013 IEEE.

| MD     | ER  | MC  | VL  | DG  |
| ------ | --- | --- | --- | --- |
| unsure |     | yes |     | yes |

* *MC* - in the abstract they say they provide "an effective selection of quality measurements", and that it's " based on the type of software". It could be useful to see why they claim their selection is "effective", and also for our Landscaping if some of them are specific to a certain kind of SW.
* *DG* - Quality measure definition may be useful

### Review

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
| 41       | Individual Information | Stakeholder's information influenced by the role involved and the type of software. |  Qualitative  |  All  | ER | Type of software can be rich client, web application and so on. |
| 41       | Stakeholder context | Detail e.g. stakeholder role and tool-usage data by each stakeholder |  Qualitative |  All | ER        |  Software architects, developers and testers are the considred essential role in the development process. |
| 41       | Technical context | Information about the source code by using e.g. software metrics |  Quantitative |  All | ER        |  Type of software can be rich client, web application and son. |
| 41       | Context-sensitive | The relation between the data, the world the data refers to, and the observer's expectations, intentions and interests |  Qualitative |  All | ER        |  The paper provides an illustrative example to support different stakeholders in the quality assessement of a software system. |



**NOTE: This article is mainly on software quality assessment than software quality definition.** However it contains an interesting approach based on stakeholder's information needs and the tailoring of information for software quality assessment. This paper also provides some guidelines to support the activities carried out by each type of stakeholders.

---

## 45 - A systematic review of quality attributes and measures for software product lines

### Montagud S., Abrahão S., Insfran E.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-84865626740&doi=10.1007%2fs11219-011-9146-7&partnerID=40&md5=33b25cd0a25fc09685e06cbc9c988f14

It is widely accepted that software measures provide an appropriate mechanism for understanding, monitoring, controlling, and predicting the quality of software development projects. In software product lines (SPL), quality is even more important than in a single software product since, owing to systematic reuse, a fault or an inadequate design decision could be propagated to several products in the family. Over the last few years, a great number of quality attributes and measures for assessing the quality of SPL have been reported in literature. However, no studies summarizing the current knowledge about them exist. This paper presents a systematic literature review with the objective of identifying and interpreting all the available studies from 1996 to 2010 that present quality attributes and/or measures for SPL. These attributes and measures have been classified using a set of criteria that includes the life cycle phase in which the measures are applied; the corresponding quality characteristics; their support for specific SPL characteristics (e. g., variability, compositionality); the procedure used to validate the measures, etc. We found 165 measures related to 97 different quality attributes. The results of the review indicated that 92% of the measures evaluate attributes that are related to maintainability. In addition, 67% of the measures are used during the design phase of Domain Engineering, and 56% are applied to evaluate the product line architecture. However, only 25% of them have been empirically validated. In conclusion, the results provide a global vision of the state of the research within this area in order to help researchers in detecting weaknesses, directing research efforts, and identifying new research lines. In particular, there is a need for new measures with which to evaluate both the quality of the artifacts produced during the entire SPL life cycle and other quality characteristics. There is also a need for more validation (both theoretical and empirical) of existing measures. In addition, our results may be useful as a reference guide for practitioners to assist them in the selection or the adaptation of existing measures for evaluating their software product lines. © 2011 Springer Science+Business Media, LLC.

| MD  | ER  | MC     | VL  | DG  |
| --- | --- | ------ | --- | --- |
| yes |     | unsure |     | yes |

* *MC* - the authors mention "165 measures related to 97 different quality attributes". It's so large that I'm unsure if it's suitable for our task. We'll need to see in detail.

### Review

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
 | 45 | Binary size | Binary size | Quantitative |  | JC | Exclude, not sure how good this criterion is |
 | 45 | Complexity of the source code | Cyclomatic complexity | Quantitative |  | JC |  |
 | 45 | Performance |  | Quantitative |  | JC |  |
 | 45 | Complexity of the source code (for classes and components) |  | Quantitative |  | JC | Requires well established software engineering practices.  Alternative: Yes/No and how (e.g., code review) |
 | 45 | Complexity of diagrams (for classes and components) |  | Quantitative |  | JC | Requires well established software engineering practices. Alternative: Yes/No and how (e.g., some sort of peer-review) |
 | 45  | Complexity of an architecture |  | Quantitative |  | JC | Requires well established software engineering practices. Alternative: Yes/No and how (e.g., some sort of peer-review) |
 | 45 | Complexity of a use case |  | Quantitative |  | JC | Requires well established software engineering practices. Alternative: Yes/No and how (e.g., some sort of peer-review) |
 | 45 | Complexity of a use case diagram |  | Quantitative |  | JC | Optional, not sure use case diagrams are always needed. Exclude |
 | 45 | Maintainability Index (MI) (for the whole, for a component, for the architecture |  | Quantitative |  | JC |  |
 | 45 | Reusability (of the whole and the components) |  | Quantitative |  | JC |  |
 | 45 | Reusability of the architecture |  | Quantitative |  | JC |  |
 | 45 | Applicability |  | Quantitative |  | JC | Validation against use cases or requirements (?) |
 | 45 | Understandability |  | Quantitative |  | JC |  |
 | 45 | Efficiency |  | Quantitative |  | JC | Exclude (difficult to measure) |
 | 45 | Effort required for changes |  | Quantitative |  | JC | Exclude (difficult to measure) |
 | 45 | Size (of modules, lines, components) |  | Quantitative |  | JC | Exclude, not sure how good this criterion is |
 | 45 | Maturity | Time for the code to fail, number of resolved bugs, number of open bugs | Quantitative |  | JC |  |
 | 45 | Configuration Complexity |  | Quantitative |  | JC | Configuration to run the code (?) |
 | 45 | Modularity of the architecture |  | Quantitative |  | JC |  |
 | 45 | Customizability |  | Quantitative |  | JC | Exclude, looks like related to customization by final user |
 | 45 | Internal cohesion |  | Quantitative |  | JC | Exclude (difficult to measure). Requires well established software engineering practices |
 | 45 | Coherence |  | Quantitative |  | JC | Exclude (difficult to measure). Requires well established software engineering practices |


---

## 46 - Standardized code quality benchmarking for improving software maintainability

### Baggen R., Correia J.P., Schill K., Visser J.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-84860465895&doi=10.1007%2fs11219-011-9144-9&partnerID=40&md5=042a7624f2cb95e1a97643ef8e0f9071

We provide an overview of the approach developed by the Software Improvement Group for code analysis and quality consulting focused on software maintainability. The approach uses a standardized measurement model based on the ISO/IEC 9126 definition of maintainability and source code metrics. Procedural standardization in evaluation projects further enhances the comparability of results. Individual assessments are stored in a repository that allows any system at hand to be compared to the industrywide state of the art in code quality and maintainability. When a minimum level of software maintainability is reached, the certification body of TÜV Informationstechnik GmbH issues a Trusted Product Maintainability certificate for the software product. © Springer Science+Business Media, LLC 2011.

| MD  | ER  | MC  | VL  | DG  |
| --- | --- | --- | --- | --- |
| yes | yes | yes |     | yes |

* *ER* - software definition, software metrics
* *MC* - related to Landscaping, since it focused on quite specific SW (standard) and criteria (maintainability). They refer to the ISO/IEC 9126 definition.

### Review

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
| 46       | Volume | Size of the software application | Quantitative | All Types | LC        | Estimated rebuild value |
| 46       | Redundancy | Level of redundancy in code | Quantitative | All Types | LC        | Percentage of redundant code |
| 46       | Unit size | Lowel-level piece of functionality that should be maintained | Quantitative | All Types | LC        | Lines of code per unit (Unit=smallest piece of invokable code) code |
| 46       | Unit complexity | Of the software application | Quantitative | All Types | LC        | Cyclomatic complexity per unit |
| 46       | Unit interface size | Number of parameters in interface | Quantitative | All Types | LC        | Number of parameters per unit |
| 46       | Module coupling |  | Quantitative | All Types | LC        | Number of parameters per unit | Number of incoming calls per module |

**Comment**

The paper presents a standardized measurement model based on the ISO/IEC 9126 definition of maintainability and source code metrics.
In this ISO standard they propose a hierarchical quality model made of quality characteristics decomposed in subcharacteristics.
They choose 6 code properties as key metrics for the quality assessment of the subcharacteristics.
Then they keep a benchmark database to perform comparison and evaluate new measurements. In this database they use metadata attributes to tag each measurement and help with comparing.

The quality characteristics from ISO/IEC 9126 they mention are:
- Analysability: measured with Volume, Redundancy and Unit size.
- Changeability: measure with Redundancy, Unit complexity and Module coupling.
- Stability: measured with Unit inteface size and Module coupling.
- Testability: measured with Unit complexity and Unit size.

---

## 58 - Quality specification and metrication, results from a case-study in a mission-critical software domain

### Trienekens J.J.M., Kusters R.J., Brussel D.C.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-77956057048&doi=10.1007%2fs11219-010-9101-z&partnerID=40&md5=8676a4867b80d63fce5b0d10d732fb63

Software quality is of increasing importance in mission-critical embedded software systems. Due to the fast growing complexity and accompanying risks of failures of these systems, software quality needs to be addressed explicitly by software developers, preferably with a systematic method for an optimal implementation of software qualities, such as reliability, time-behavior and usability. At the Centre of Automation of Mission-critical Systems (CAMS) of the Dutch Royal Navy, a new approach has been defined for software developers to improve the way that they deal with software quality in the process of mission-critical systems engineering. The stepwise approach is based on both an international quality standard for software product quality, i.e. ISO9126, and on Multi-Criteria Decision Making techniques, i.e. analytical hierarchy process (AHP). The stepwise approach has been validated in a case study. In particular, the tailoring of the ISO9126 standard toward the specific CAMS development situation, and the applicability of AHP techniques, from the perspective of software developers, has been investigated. The case study is carried out in a representative software development project, i.e. the software for combat management systems (CMS) of warships. Results of the case study show that software developers can explicitly deal with quality on the basis of both the ISO9126 standard and the AHP techniques, respectively regarding the specification, prioritization and metrication of software product quality. © 2010 The Author(s).

| MD  | ER     | MC  | VL  | DG  |
| --- | ------ | --- | --- | --- |
| yes | unsure | yes |     | yes |

* *ER* - software metrics
* *MC* - a good example of criteria for a specific type of software (critical systems).

### Review

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
 | 58 | real-time performance |  | Quantitative | critical systems (non exclusive) | MC |  |
 | 58 | reliability | mission specific | Quantitative | critical systems (non exclusive) | MC |  |
 | 58 | consistency | same rules along SW development process | Quantitative | | MC |  |
 | 58 | transparency | | Quantitative | | MC |  |
 | 58 | usability | feedback from final users | Qualitative | | MC |  |
 | 58 | effectiveness | useful for final users | Quantitative | | MC |  |
 | 58 | productivity | fast results from final users | Quantitative | | MC |  |
 | 58 | usability | easy to use by final users | Quantitative | | MC |  |
 | 58 | safety |  not prone to error by final users | Quantitative | | MC |  |
 | 58 | satisfaction |  feedback from final users | Qualitative | | MC |  |
 | 58 | maintainability |  Easy to modify according to changing needs | Quantitative | | MC |  |
 | 58 | portability | Easy to implement in different scenarios | Quantitative | | MC |  |
---

## 61 - Software quality models: Purposes, usage scenarios and requirements

### Deissenboeck F., Juergens E., Lochmann K., Wagner S.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-78049485828&doi=10.1109%2fWOSQ.2009.5071551&partnerID=40&md5=8fcbe52cf221d20710deaf02231c9c19

Software quality models are a well-accepted means to support quality management of software systems. Over the last 30 years, a multitude of quality models have been proposed and applied with varying degrees of success. Despite successes and standardisation efforts, quality models are still being criticised, as their application in practice exhibits various problems. To some extent, this criticism is caused by an unclear definition of what quality models are and which purposes they serve. Beyond this, there is a lack of explicitly stated requirements for quality models with respect to their intended mode of application. To remedy this, this paper describes purposes and usage scenarios of quality models and, based on the literature and experiences from the authors, collects critique of existing models. From this, general requirements for quality models are derived. The requirements can be used to support the evaluation of existing quality models for a given context or to guide further quality model development. © 2009 IEEE.

| MD  | ER  | MC  | VL  | DG  |
| --- | --- | --- | --- | --- |
| yes | yes | yes |     | yes |

* *ER* - it should explain software characteristics critically
* *MC* - related to Landscaping at least. The tackle a specific problem: "there is a lack of explicitly stated requirements for quality models with respect to their intended mode of application".

### Review

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment   |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-------: |
| 61       | n/a   | n/a        | n/a                      | n/a            | MD        | See below |

* *MD* - The paper does not define any Quality Model, or set of criteria or attributes, instead it
defines how to make (requirements) for new Quality models. Nonetheless, it identifies three types of
models:
  * taxonomic models like the ISO 9126 - *Define Quality*
  * metric-based models like the maintainability index (MI) - *Assess Quality*
  * stochastic models like reliability growth models (RGMs) - *Predict Quality*

* May be interesting for landscaping (see figure 1: DAP Classification for Q-Models). 

---

## 74 - Continuous software quality supervision using source inventory and columbus

### Bakota T., Beszédes A., Ferenc R., Gyimóthy T.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-57349138856&doi=10.1145%2f1370175.1370193&partnerID=40&md5=da38b72dde1093c2ee7dba33829c5806

Several tools and methods for source code quality assurance based on static analysis finally reached a state when they are applicable in practice and recognized by the industry. However, most of these tools are used in an isolated manner and very rarely as organic parts of the quality assurance process. Furthermore, little or no help is provided in interpreting the outputs of these tools. This paper presents Source Inventory, a system for source code-based software quality assessment and monitoring, which is able to collect, store and present measurement data including metrics, coding problems and other kinds of data like bug numbers and test coverage information. It helps software developers, architects and managers to take control over their software's quality by performing continuous code scans, fault detection, coding style verification, architecture violation detection, and automatic report generation considering metric baselines.

| MD  | ER  | MC  | VL  | DG     |
| --- | --- | --- | --- | ------ |
| yes |     | yes |     | unsure |

* *MC* - related to Perspectives of developers.

### Review

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
| 74       |  n/a  | n/a  | n/a  | C/C++ based software  | MT        |  See below       |

Comment

The paper (very) briefly describes SourceInventory, a system that provides a set of quantitative metrics presented in a user-friendly graphical interface. According to the authors, those metrics are suitable for quality assessment and automatic supervision of code-based software. The paper published in 2008 is just two pages long. It does not contain any helpful information to understand how the tool works or any info related to the underneath technology. However, it is (was) based on the Columbus technology described in a different paper (published in 2002). 

It seems that the SourceInventory system has been superseded by some other tools commercialized by the same spin-off of Szeged University, whose some members wrote the paper. More info here: http://www.frontendart.com.

---

## 82 - The EMISQ method - Expert based evaluation of internal software quality

### Plösch R., Gruber H., Hentschel A., Körner Ch., Pomberger G., Schiffer S., Saft M., Storck S.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-47749132628&doi=10.1109%2fSEW.2007.71&partnerID=40&md5=cd7975c8b3e6f9fec2a175545c539b15

Internal software quality, e.g. the quality of code, has great impact on the overall quality of software. Besides well known manual inspection and review techniques more recent approaches utilize tool-based static code for the evaluation of internal software quality. Despite the high potential of static code analyzers the application of tools alone cannot replace well founded expert opinion. Knowledge, experience and fair judgement is indispensable for a valid, reliable quality assessment, which is accepted by software developers and managers. The EMISQ method (Evaluation Method for Internal Software Quality), guides the assessment process for all stakeholders of an evaluation project. The method is supported by a tool that assists evaluators with their analysis and rating tasks and provides support for generating a code quality report. The application of the method in a pilot project has shown its applicability.

| MD  | ER  | MC     | VL  | DG  |
| --- | --- | ------ | --- | --- |
| yes |     | unsure | yes | yes |

* *MC* - this seems to be proposing some kind of methodology, rather than criteria. We should to check how objective it is.

### Review

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment   |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-------: |
| 82       | n/a   | n/a        | n/a                      | n/a            | MV        | See below |

* *MV* - this paper indeed describes the "EMISQ" approach to internal(*) software quality assessment
  ("internal" as in "quality aspects that are primarily visible to software architects, developers and testers").
  The overall idea is to combine static analysis tools with expert input, for which EMISQ provides a framework.
  It provides a corresponding quality model, but seemingly without describing the quality criteria in significant
  detail. For this, the reader is referred to the ISO 9126 quality model and the following static analysis tools
  (primarily aimed at C++ and Java code, apparently):

  - CPD: https://pmd.github.io/latest/pmd_userdocs_cpd.html
  - FindBugs: http://findbugs.sourceforge.net
  - JLint: http://jlint.sourceforge.net/
  - JMetric: https://sourceforge.net/projects/jmetric/
  - PC-Lint: https://gimpel.com/
  - PMD: https://pmd.github.io/
  - QJPro: http://qjpro.sourceforge.net/

  (*) The distinction between "internal" and "external" quality aspects seems to be a useful one:

  - "internal software quality": "quality aspects that are primarily visible to software architects, developers and testers":

    - "[...] has a high impact on the external quality and is thus an important part of quality assurance."
    - "[...] focuses on the source code, internal documentation, architectural descriptions, etc."
    - "no knowledge about the functional and non-functional specification of the software product is needed nor must the software be executable"

  - "external software quality": "quality aspects that are noticeable by the users of a software product":

    - "Typical [...] attributes are usability, functionality and efficiency."
    - "[...] requires an operational product that has to be executed in order to be evaluated."


---

## 83 - In search for a widely applicable and accepted software quality model for software quality engineering

### Côté M.-A., Suryn W., Georgiadou E.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-36549049028&doi=10.1007%2fs11219-007-9029-0&partnerID=40&md5=59c39869ee11beea4f39ae055a8804c0

Software Quality Engineering is an emerging discipline that is concerned with improving the approach to software quality. It is important that this discipline be firmly rooted in a quality model satisfying its needs. In order to define the needs of this discipline, the meaning of quality is broadly defined by reviewing the literature on the subject. Software Quality Engineering needs a quality model that is usable throughout the software lifecycle and that it embraces all the perspectives of quality. The goal of this paper is to propose the characteristics of a quality model suitable for such a purpose, through the comparative evaluation of existing quality models and their respective support for Software Quality Engineering. © 2007 Springer Science+Business Media, LLC.

| MD  | ER  | MC  | VL  | DG  |
| --- | --- | --- | --- | --- |
| yes |     | yes | yes | yes |

* *MD* - comparative evaluation of existing quality models
* *MC* - I expect this one to have a complete comparison of other methodologies.

### Review

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
| 83       | n/a   | n/a        | n/a                      | n/a            | VL        | See below |


The paper dates from 1998. It aims to compare software quality models that respond to different points of view: user, compliance with specifications and quality of the engineering process, inherent quality of the product.

4 models are compared: McCall model, Boehm model, Droney model, ISO/IEC 9126 standard.
The criteria that stand out: portability, reliability, efficiency, usability, maintainability
But there is no real precision on indicators or measurements on these different criteria.
The interesting point is the different perspectives.

---

## 85 - Achieving quality in open-source software

### Aberdour M.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-33846917203&doi=10.1109%2fMS.2007.2&partnerID=40&md5=08d47741430e05c8a0ceb015a1f43a04

The open source software community has published a substantial body of research on OSS quality. Focusing on this peer-reviewed body of work lets us draw conclusions from empirical data rather than rely on the large volume of evangelical opinion that has historically dominated this field. This body of published research has become much more critical and objective in its efforts to understand OSS development, and a consensus has emerged on the key components of high-quality OSS delivery. This article reviews this body of research and draws out lessons learned, investigating how the approaches used to deliver high-quality OSS differ from, and can be incorporated into, closed-source software development. © 2007 IEEE.

| MD  | ER  | MC  | VL  | DG  |
| --- | --- | --- | --- | --- |
| yes |     | yes | yes | yes |

### Review

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
| 85       | Code documentation | The code is documented      | Qualitative and quantitative | all types | DG        | See below |
| 85       | Sustainable community | Is there an active community behind the software product? (i.e., for maintenance/bug fixing) | both |  all types              | DG        | See below |
| 85       | Code modularity   | The code of the project is not a whole entity, but is fragmented in smaller modulues that make it easier to contribute to | Quantitative | all types | DG        | See below |
| 85       | Code goes through code reviews/peer review | Each contribution is assessed by a contributor different from the author |  Qualitative                        | All types  | DG        | See below |
| 85       | Tests | Each method/function has a test to support it | Quantitative | all types | DG        | See below |
| 85       | Tutorials | Availability of material explaining how to use the target software through examples | Qualitative/Quantitative | All types  | DG        | See below |


**Comment**:

The paper focuses on project management for quality, comparing open source software projects with non open initiatives.
- Quality areas: quality assurance (focuses on process and procedure, learning from mistakes, and ensuring good management practice) and quality control (process of verification and validation)

---

## 88 - Driving software quality: How test-driven development impacts software quality

### Crispin L.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-33846907119&doi=10.1109%2fMS.2006.157&partnerID=40&md5=1c6ac14fdd83073f861f9ec5b1e95701

Recently, software development teams using agile processes have started widely adopting test-driven development. But does TDD really improve software quality? © 2006 IEEE.

| MD  | ER  | MC  | VL  | DG     |
| --- | --- | --- | --- | ------ |
| yes |     |     | yes | unsure |

* *DG* - Abstract does not provide many details

### Review

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
| 88       | Test driven development | Definition and development of unit tests for each functionality | Quantitative | All | ER |  |
| 88       | Project creole      | A shared language (between manager and developers)           | Qualitative: managers can improve the way they define features, developers can easily produce well-tailored program  | All | ER | It considers important the development of a shared language or project creole between business people and developers to find some common ground and work together in order to improve software development.  |

**NOTE: this is a paper of 2 pages**. For my point of view it can be left out for quality definition. 


---

## 92 - Software quality development and assurance in RUP, MSF and XP -A comparative study

### Zuser W., Heil S., Grechenig T.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-84885903144&doi=10.1145%2f1083292.1083300&partnerID=40&md5=c47fec6c93dd2cc890ba61b5ce2ab7c1

The support of software quality in a software development process may be regarded under two aspects: first, by providing techniques, which support the development of high quality software and second, by providing techniques, which assure the required quality attributes in existing artifacts. Both approaches have to be combined to achieve effective and successful software engineering. In this study, we compare three of the most industrially relevant software development process models (Rational Unified Process (RUP), Microsoft Solution Framework (MSF) and Extreme Programming (XP)) regarding their software quality support in terms of software quality development and software quality assurance. Based on the results we propose a de-facto standard for quality support in software development process models. © 2005 ACM.

| MD  | ER  | MC  | VL  | DG  |
| --- | --- | --- | --- | --- |
| yes |     | yes | yes | yes |

### Review

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
| 92       |       |            |                          |                | JC        |         |

---

## 93 - Early estimation of software quality using in-process testing metrics: A controlled case study

### Nagappan N., Williams L., Vouk M., Osborne J.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-77955433687&doi=10.1145%2f1083292.1083304&partnerID=40&md5=c3b21a87b407b65539153ab3017b0eda

In industrial practice, information on post-release field quality of a product tends to become available too late in the software development process to affordably guide corrective actions. An important step towards remediation of this problem of late information lies in the ability to provide an early estimation of software post-release field quality. This paper presents the use of a suite of in-process metrics that leverages the software testing effort to provide (1) an estimation of potential software field quality in early software development phases, and (2) the identification of low quality software programs. A controlled case study conducted at North Carolina State University provides initial indication that our approach is effective for making an early assessment of post-release field quality. © 2005 ACM.

| MD     | ER  | MC     | VL  | DG     |
| ------ | --- | ------ | --- | ------ |
| unsure |     | unsure | yes | unsure |

* *MC* - we can check if they provide actual criteria for quality assessment.
* *DG* - The software quality metrics could be interesting... 

### Review

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
| 93       | Test quantification SM1 | Number of Assertions SLOC* | Quantitative | Java code | LC        | Accounts for coding/testng style |
| 93       | Test quantification SM2 | Number of Test Cases SLOC* | Quantitative | Java code | LC        | Accounts for coding/testng style |
| 93       | Test quantification SM3 | Number of Assertions divided by Number of Test Cases | Quantitative | Java code | LC        | Accounts for coding/testng style |
| 93       | Test quantification SM4 | (TLOC/SLOC*)  divided by (Number of Classes Test Number of ClassesSource) | Quantitative | Java code | LC        | Serves as a control measure to counter the confounding effect of class size |
| 93       | Cyclomatic complexity | Relative ratio of test to source code in Cyclomatic Complexity | Quantitative | Java code | LC        | Complexity and O-O metrics |
| 93       | CBO  | Relative ratio of test to source code in Coupling between objects | Quantitative | Java code | LC        | Complexity and O-O metrics |
| 93       | DIT  | Relative ratio of test to source code in Depth of Inheritance | Quantitative | Java code | LC        | Complexity and O-O metrics |
| 93       | WMC  | Relative ratio of test to source code in  weighted methods per class | Quantitative | Java code | LC        | Complexity and O-O metrics |
| 93       | Relative size adjustment  | SLOC* divided by Minimum SLOC* | Quantitative | Java code | LC        | Complexity and O-O metrics |

\* Source Lines of Code (SLOC) is computed as non-blank, non-comment source lines of code

\+ Test Lines of Code (TLOC) is computed as non-blank, non-comment test lines of code

**Comment**

They present a metric suite called the Software Testing and Reliability Early Warning metric suite for Java (STREW-J) that can be used as an early indication of an external measure of software application quality. They put a greater emphasis on internal software metrics, particularly those involving the testing effort. It requires the existence of an extensive suite of automated unit test cases being created as development proceeds.

---

## 99 - The evolution path for industrial software quality evaluation methods applying ISO/IEC 9126:2001 quality model: Example of MITRE's SQAE method

### Côté M.-A., Suryn W., Laporte C.Y., Martin R.A.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-17444388547&doi=10.1007%2fs11219-004-5259-6&partnerID=40&md5=09ec05c221610b4c799ab6111def6568

This paper examines how the industrial applicability of both ISO/IEC 9126:2001 and MITRE Corporation's Software Quality Assessment Exercise (SQAE) can be bolstered by migrating SQAE's quality model to ISO/IEC 9126:2001. The migration of the quality model is accomplished through the definition of an abstraction layer. The consolidated quality model is examined and further improvements to enrich the assessment of quality are enumerated. © 2005 Springer Science + Business Media, Inc.

| MD  | ER  | MC  | VL  | DG  |
| --- | --- | --- | --- | --- |
| yes |     | yes | yes | yes |

* *MC* - perhaps too specific, but this one provides a case study on the applicability of ISO/IEC 9126.

### Review

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: | 
 | 99 | consistency | in many aspects of ISO/EIC 9126 | Quantitative | | MC |  |
 | 99 | independence | interoperativity, changeability, adaptability | Quantitative | | MC |  |
 | 99 | modularity | changeability, testability | Quantitative | | MC |  |
 | 99 | documentation | learnability, analysability | Quantitative | | MC |  |
 | 99 | self-descriptiveness | understandability, operability, analysability | Quantitative | | MC |  |
 | 99 | anomaly-control | maturity, fault tolerance, recoverability, reliability compliance | Quantitative | | MC |  |
 | 99 | design simplicity | security, analysability, changeability, stability, testability | Quantitative | | MC |  |
 
Mainly a correlation between their proposed quality factors and the sub-characteristics in ISO/EIC 9126.

---

## 101 - Measuring software product quality: A survey of ISO/IEC 9126

### Jung H.-W., Kim S.-O., Chung C.-S.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-4644328140&doi=10.1109%2fMS.2004.1331309&partnerID=40&md5=806cc089be00baf45f49985bf0cd1cdd

A user survey was carried out to evaluate empirically ISO/IEC 9126's dimensionality, or the classification of characteristics, and internal- consistency reliability. In the survey, users evaluated their satisfaction concerning the quality of a packaged software product according to the criteria of ISO/IEC 9126's subcharacteristics. Overall, results reveal ambiguities in the way that ISO/IEC 9126 is structured in terms of characteristics and subcharacteristics.

| MD  | ER  | MC  | VL  | DG     |
| --- | --- | --- | --- | ------ |
| yes | yes | yes |     | unsure |

* *ER* - however it depends on its content, because ISO/IEC 9126 has been revised by ISO/IEC 25010:2011. 
* *MC* - article 99 also refers to ISO/IEC 9126. It'd be interesting to describe what are the novelties in ISO/IEC 25010:2011.
* *DG* - I am unsure because this is a user survey based on existing models. We should probably focus on the models... 

### Review

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment --|
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-------: |
| 101      | n/a   | n/a        | n/a                      | n/a            | MD        | See below |

* *MD* - paper describes a survey and analysis of ISO/IEC 9126.
  * It does not define per se any SQ attributes or criteria. Refer to ISO/IEC 9126 for that definition.
  * The paper may still be relevant if we want to show how difficult and ambiguous it is to evaluate ISO/IEC 9126
    characteristics to a real world SW by actual users and developers.

---

## 108 - Construction of a systemic quality model for evaluating a software product

### Ortega M., Pérez M., Rojas T.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-3543054780&doi=10.1023%2fA%3a1025166710988&partnerID=40&md5=f6915840807fb5204c5c331644d47524

Quality is currently considered one of the main assets with which a firm can enhance its competitive global position. This is one reason why quality has become essential for ensuring that a company's products and processes meet customers' needs. A recent innovation in the systems area is the development of a set of mechanisms and models for evaluating quality. This article describes the design of a Quality Model with a systemic approach to software products that assesses a product's efficiency and effectiveness. Different quality models were studied: McCall, Boehm, FURPS, ISO 9126, Dromey, ISO 15504 in an attempt to identify the aspects present in these models that are deemed important in a Systemic Quality model. We designed a model prototype that reflects the essential attributes of quality. This model was evaluated using a method so it can be validated and also enhanced. The evaluation method consisted of: designing a survey, formulating, validating and applying the measurement instruments; defining an algorithm to obtain the quality estimate and analyzing the results. The model prototype enabled the strengths and weaknesses of the software products studied to be identified. When evaluating a software product using the model prototype, it was possible to ascertain its compliance with the standards and use the results to improve it. Since the evaluation was systemic, processes that affect certain characteristics of the product could be identified. Companies can benefit from the model proposed because it serves as a benchmark that allows their products to evolve and be competitive.

| MD  | ER  | MC  | VL  | DG  |
| --- | --- | --- | --- | --- |
|     | yes | yes |     | yes |

* *ER* - it should identify set of attributes that overlaps various models

### Review

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
| 108      | Systemic model | Extends ISO9126, Dromey and McCall models  |  Mainly qualitative: set of measures and practices   |   all   | MT   | See below     |

Comment

The study proposes a systemic quality model. Authors developed a process framework with which to evaluate product quality considering the processes that contribute to product
quality. They basically extend ISO 9126 product quality model considering the roles of stakeholders (project managers, developers, and users) trying to evaluate the internal quality,
which includes functionality, reliability, usability, efficiency, maintainability, and portability characteristics. Authors claimed that those quantities relate to each other and must
be integrated for a systemic global quality design. The work does not analyze the effect of the method applied on different stakeholders.

---

## 112 - Multi-Criteria Methodology Contribution to the Software Quality Evaluation

### Blin M.-J., Tsoukiàs A.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-0011893888&doi=10.1023%2fA%3a1016626919680&partnerID=40&md5=a137d99a58bbb4836370b1d4ff3554bc

Industrial evaluations of COTS software largely used the quality models provided by the international standards. But the context and objectives of COTS evaluations are fundamentally different than those primarily defined by the standards. Several key issues are often forgotten: (1) the existence of several evaluators and several quality models sharing common factors, criteria and measures, (2) the purpose of the evaluation model, (3) measures of different types, and (4) the recursive nature of the model since each node is an evaluation model itself. We had the occasion to study the results of real standard-based COTS evaluations. Faced with the difficulties to exploit them, we experimented the use of multi-criteria methodology. This work allows us to understand some of the problems generated by the application of the standards to COTS evaluations, and to propose new principles for evaluating software quality that should be considered in an evolution of the standards. This paper reports our experiment.

| MD  | ER  | MC  | VL  | DG  |
| --- | --- | --- | --- | --- |
| yes |     | yes |     | yes |

* *MC* - this one is specifically on criteria for quality. I expect a detailed review and discussion in this article.


### Review

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment   |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-------: |
| 112      | n/a   | n/a        | n/a                      | n/a            | MV        | See below |

* *MV* The main message of this paper is that care should be taken when using the ISO 9126 and IEEE 1061
  standard in software quality evaluations, because:

  1. "[...] a single evaluation model is applied all along the hierarchy of evaluation nodes neglecting important
    variations due to the presence of different evaluators, of software components and of evaluation purposes."

  2. "[...] the unjustified use of a single aggregation procedure all along the hierarchy (the weighted sum), [...]"

  As such, the paper does not seem to discuss actual (individual) quality criteria -- for these, the above
  standards are relied upon. But their main message could still be relevant for us, as it applies to the calculation
  of a global quality measure from the individual quality factors and their weights (which may furthermore differ
  between the different evaluators). The authors discuss 3 alternatives to the typical arithmetic mean (i.e. weighted
  average) that is used to this end: (1) ordinal aggregation, (2) geometric means, and (3) dual geometric means.
  The authors' recommendation seems to be to consider the information from all 3 aggregation procedures.

  (Note: the "COTS" acronym is not defined in the paper, but seems to stand for "commercial off-the-shelf".)


---

## 116 - Software quality analysis & measurement service activity in the company

### Tanaka Takeshi, Aizawa Minoru, Ogasawara Hideto, Yamada Atsushi

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-0031597187&doi=10.1109%2fICSE.1998.671598&partnerID=40&md5=377b5ac3a4b038bfd392e01d4e7c6600

It is very important to improve software quality using program analysis & measurement tools and SQA (Software Quality Assurance) method at the appropriate points during the process of development. But in many development departments, there is often not enough time to evaluate and use the tools and SQA method or to accumulate the know-how for effective use. This paper describes the support activity of a software quality analysis & measurement service which is performed by our team of laboratory within the company as a third-party independent staff group. We call this activity HQC (High Quality software creation support virtual Center). The purpose of this activity is as follows. First we improve the software quality engineering process in the development department, for example, we help them to increase efficiency of review or testing. To accomplish this, we use program static analysis tools to detect fault-prone software components. Next we assist in starting their own self-improvement process. In addition, we provide service activity to many development departments concurrently. We have been making progress with these activities, and some development departments have begun to establish improvement process themselves.

| MD  | ER  | MC     | VL  | DG     |
| --- | --- | ------ | --- | ------ |
| yes |     | unsure |     | unsure |

* *MC* - I'm not sure if this one is about quality itself, or to optimize processes in which quality is improved.

### Review

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
| 116      | n/a   | n/a        | n/a                      | n/a            | VL        | See below |

The paper dates from 1998 and describes the implementation of a service to help software quality at Toshiba.

It describes rather the organization set up, and is centered on the static analysis with indicators on the graphical interface part (number of events, screens...) and metrics on the back part corresponding to the static analysis of the files without more details.

---

## 118 - A critical look at ISO 9000 for software quality management

### Stelzer D., Mellis W., Herzwurm G.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-0642363924&doi=10.1023%2fA%3a1018591430752&partnerID=40&md5=9181348bb75865be23649ef29338594f

A considerable number of software suppliers report improvements in product and service quality, development costs and time to market achieved with the help of the ISO 9000 standards. Nevertheless, the ISO 9000 family has received unfavourable criticism in journals, textbooks and at software quality conferences. The paper summarizes, discusses and reviews eleven of the most popular arguments against the ISO 9000 standards. The review of the criticism is based on findings of two empirical surveys among European software suppliers that have implemented an ISO 9000 quality system. The paper concludes with suggestions and guidelines for advances in software quality management concepts, such as the ISO 9000 family, CMM, BOOTSTRAP and the emerging SPICE standard.

| MD  | ER  | MC  | VL  | DG  |
| --- | --- | --- | --- | --- |
| yes |     | yes |     | yes |

* *MC* - any works that are critical with quality standards or methodologies is important, since they're very likely to discuss about their weaknesses and provide hints on how to improve them.

### Review

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
| 118      |       |            |                          |                | IC        |         |

---

## 120 - Specifying software quality with the extended ISO model

### Van Zeist R.H.J.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-27144550799&doi=10.1007%2fBF00209185&partnerID=40&md5=64394714677ede47867fcd1a5625efff

Specifying the quality of software products is a valuable addition to functional specification, clarifying product properties such as learnability and availability. Specifying such properties is considered difficult due to the different parties involved and the implicit nature of the requirements. The QUINT project gathered experience with product specification by means of the Extended ISO model: an extension to the ISO 9126 model of software quality. By defining indicators and specifying how they should be measured, quality specifications can make requirements explicit. Recommendations and pitfalls for composing a specification are grouped by the context in which quality specifications can be used. © 1996 Chapman & Hall.

| MD  | ER  | MC  | VL  | DG  |
| --- | --- | --- | --- | --- |
|     |     | yes | yes | yes |

* *MC* - same comments as for 118: articles describing "pitfalls" of weaknesses are very informative.

### Review

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
| 120      |       |            |                          |                | IC        |         |

---

## 123 - Building quality into scientific software

### Hovenden F.M., Walker S.D., Sharp H.C., Woodman M.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-0038778889&doi=10.1007%2fBF02420942&partnerID=40&md5=bece44920d4927c101c2305f0b37fbe9

This paper has developed from the SoFEA project at The open University which is studying the non-technical aspects of quality in software. This involves seeing the technical elements of software development as very much part of a wider context. The culture of an organization as a whole, particularly its management strategies, are regarded as driving and shaping the technology. A particular challenge for management we have observed is how to harmonize a skilled individualist (affectionately dubbed a 'maverick') and a quality management system. We explore the characteristics of an individualist programmer and discuss the options for managing such a person. Some of the experiences of a scientific organization are reported. © 1996 Chapman & Hall.

| MD  | ER  | MC  | VL  | DG     |
| --- | --- | --- | --- | ------ |
|     |     | yes | yes | unsure |

* *MC* - important for Landscaping and to identify practices which might be specific to certain disciplines (such as scientific or research software).
* *DG* - The paper seems to focus on quality management, rather than defining quality dimensions

### Review

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
| 123      |       |            |                          |                | DG        |         |

---

## 124 - Software quality: the elusive target

### Kitchenham Barbara, Pfleeger Shari Lawrence

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-0029779819&doi=10.1109%2f52.476281&partnerID=40&md5=0c903484c06cd79cb57e3161badfff3d

High-profile disasters and the ensuing debates in the press are alerting more people to the crucial nature of software quality in their everyday lives. This should prompt software professionals to take a second look at how they define software quality. In this task of assessing 'adequate' quality in a software product, context is important. Errors tolerated in word-processing software may not be acceptable in control software for a nuclear power plant. Thus, the meanings of 'safety-critical' and 'mission-critical' must be reexamined in the context of software's contribution to the larger functionality and quality of products and businesses. At the same time, software professionals must ask themselves who is responsible for setting quality goals, and make sure they are achieved.

| MD  | ER  | MC  | VL     | DG  |
| --- | --- | --- | ------ | --- |
|     |     | yes | unsure | yes |

* *MC* - this should be useful for Landscaping also. Another example of criteria for quality which is different according to the domain. Here the mention a "nuclear power plant" (critical systems?).

### Review

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
| 124      |       |            |                          |                | ER        |         |

---

## 128 - Experiences of software quality management using metrics through the life-cycle

### Ogasawara Hideto, Yamada Atsushi, Kojo Michiko

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-0029516009&partnerID=40&md5=68106def0b53f2f1a609753364cb4705

Many software quality metrics to objectively grasp software products and process have been proposed in the past decades. In actual projects, quality metrics has been widely applied to manage software quality. However, there are still several problems with providing effective feedback to intermediate software products and the software development process. We have proposed a software quality management using quality metrics which are easily and automatically measured. The purpose of this proposal is to establish a method for building in software quality by regularly measuring and reviewing. This paper outlines a model for building in software quality using quality metrics, and describes examples of its application to actual projects and its results. As the results, it was found that quality metrics can be used to detect and remove problems with process and products in each phase. Regular technical reviews using quality metrics and information on the change of the regularly measured results was also found to have a positive influence on the structure and module size of programs. Further, in the test phase, it was found that with the proposed model, the progress of corrective action could be quickly and accurately grasped.

| MD  | ER  | MC  | VL  | DG  |
| --- | --- | --- | --- | --- |
|     |     | yes | yes | yes |

### Review

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
| 128      |       |            |                          |                | JC        |         |

---

## 129 - Controlling and predicting the quality of space shuttle software using metrics

### Schneidewind N.F.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-0343935307&doi=10.1007%2fBF00404649&partnerID=40&md5=b99281a03e36e4acaf4ca5067792314f

Software quality metrics have potential for helping to assure the quality of software on large projects such as the Space Shuttle flight software. It is feasible to validate metrics for controlling and predicting software quality during design by validating metrics against a quality factor. Quality factors, like reliability, are of more interest to customers than metrics, like complexity. However quality factors cannot be collected until late in a project. Therefore the need arises to validate metrics, which developers can collect early in a project, against a quality factor. We investigate the feasibility of validating metrics for controlling and predicting quality on the Space Shuttle. The key to the approach is the use of validated metrics for early identification and resolution of quality problems. © 1995 Chapman & Hall.

| MD  | ER  | MC  | VL     | DG  |
| --- | --- | --- | ------ | --- |
|     |     | yes | unsure | yes |

* *MC* - useful for Landscaping. I expect criteria for quality applied to critical systems here.

### Review

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
| 129      |       |            |                          |                | LC        |         |

---

## 133 - Software quality standards in practice: the limitations of using ISO-9001 to support software development

### Avison D.E., Shah H.U., Wilson D.N.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-0642350288&doi=10.1007%2fBF00213633&partnerID=40&md5=be0ebcd16c03c9f6fa5176748491b323

Quality management standard BS5740/ISO9001 is a key technology for UK and Europe in the 1990s. This paper shows that the relevance of BS5750/ISO9001 is limited and suggests that standards bodies must develop and endorse new standards to ensure that software quality improvement programmes continue to be adopted by the information technology industry. © 1994 Chapman & Hall.

| MD  | ER  | MC  | VL     | DG  |
| --- | --- | --- | ------ | --- |
|     |     | yes | unsure | yes |

* *MC* - it discusses limitations, so it should provide insights about what is missing in the standards.

### Review

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
| 133      |   NA   |     NA     |           NA             |     NA          | MC        |    Not applicable (NA)     |

This paper is specifically on the ISO-9001 standard, which are general organizational recommendations, not directly related to software.
The ISO-90003 standard (https://webstore.iec.ch/preview/info_isoiecieee90003%7Bed1.0%7Den.pdf) is about advice to applying these recommendations to organizations dealing with software as a product. However, ISO-90003 is about organization of companies, but again not about software engineering itself. Therefore, neither ISO-9001 nor any of the following revisions or specific applications of the standard is of our interest.
This paper is not applicable to our study.

---

## 140 - Modelling software quality in the commercial environment

### Gillies A.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-0001332319&doi=10.1007%2fBF01720924&partnerID=40&md5=a0b468b060b629ea3ced5fefac2c2848

Achieving quality is a perennial problem in software development. It is commercially significant because of the large sums of money spent correcting problems within information systems. The literature shows how various theoretical treatments have developed since the late 1970s. However, many of these models are of academic interest only, because they are not perceived by IT professionals to meet their needs. This article describes a study which examined the nature of quality in six different commercial environments. The aim of the study was to provide models of quality appropriate to individual commercial environments and to examine similarities between them. The results, expressed in terms of quality criteria and the relationships between them, highlight the limitations of many theoretical treatments, in particular, the highly technical view of software quality enshrined in early models, and the need for criteria contributing to 'business correctness'. The results from the study are used to highlight some of the important issues in software quality within commercial environments and some of the reasons why quality is often poor. © 1992 Chapman & Hall.

| MD  | ER  | MC  | VL  | DG  |
| --- | --- | --- | --- | --- |
| yes |     |     | yes | yes |

* *MD* - commercial SW, comparison in different SW.
* *MC* - Landscaping. Different criteria depending on the application type ("commercial" here). SW in production.

### Review

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
| 140      |       |            |                          |                | MD        |         |

---

## 144 - Practice of quality modeling and measurement on software life-cycle

### Hirayama Masayuki, Sato Hiroyuki, Yamada Atushi, Tsuda Junichiro

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-0025022794&partnerID=40&md5=155e3e9926c8e675616e8d839798a6e1

The authors introduce quality metrics into the quantitative software quality estimation technique, embracing the quality estimate of design, as well as of the source code, in studying a quality quantification support system. They outline a quality quantification technique for this system, describe examples of both its application to actual projects and its evaluation, and consider its relationship conventional techniques for estimate indexing of T. J. McCabe (IEEE Trans. Softw. Eng., vol. SE-2, no. 4, 1976) and M. H. Halstead (Elements of Software Science, North Holland, NY, 1977).

| MD         | ER  | MC  | VL  | DG  |
| ---------- | --- | --- | --- | --- |
| yes/unsure |     | yes | yes | yes |

* *MC* - if use cases are discussed, it should provide some criteria of quality. Moreover, it's "quantitative".

### Review

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
| 144      | ESQUT | It is a source code quality index  |  Quantitative            |  (old) C code  | MT        | See below  |

Comment

The paper's main motivation is that Halstead's and McCabe's metrics are not practical and have some limitations (in the case of programs with GOTO statements and deep nesting). The authors propose a new quantitative metric called ESQUT-C (for C programs) considering:
 - n. of GOTO statements
 - n. of module exits
 - n. of conditional statements
 - n. of procedure blocks
 - nesting level of procedure blocks
 - number of executions
 - number of lines (LOC)
 - number of real digits

They also showed how those metrics correlate with McCabe's and Halstead's metrics.
The paper has been published in 1990.

---

## 145 - Software Quality Assurance for Maintenance

### Collofello J.S., Buck J.J.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-0042984162&doi=10.1109%2fMS.1987.231418&partnerID=40&md5=c58510c37ada8347e2c7b69b25c6c346

Maintenance plays a vital role in protecting quality as a system evolves. The results of this study pinpoint how to make maintenance a SQA. Copyright © 1987 by The Institute of Electrical and Electronics Engineers, Inc.

| MD  | ER  | MC  | VL  | DG     |
| --- | --- | --- | --- | ------ |
| yes |     | yes | yes | unsure |

* *MD* - for Maintenance, may be interesting for our section "Release, Support, Maintenance, Usability, Reproducibility"
* *DG* - Abstract is not very informative

### Review

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment   |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-------: |
| 145      | n/a   | n/a        | n/a                      | n/a            | MV        | See below |

* *MV* - The paper presents bug-origin-statistics and lessons learned during a software maintenance effort for
   "a large, Centrex-type telephone switching system" (it's from 1987). The introduction is more general and could
   be interesting to summarize here -- they list 3 central issues when it comes to software maintenance:

   1. "the difficulty of performing maintenance activities":
      "The primary difficulty in performing maintenance tasks stems from the fact that
      the complexity of large systems increases dramatically over time, largely due to
      deteriorating program structure. This difficulty is compounded by inaccurate,
      outdated documentation and flagrant violations of programming standards."

   2. "the high degree of error associated with performing maintenance tasks":
      "often a direct result of the programs' increasing complexity"

   3. "the low morale of software maintainers":
      "[...] lack of modern software-engineering and QA approaches in software maintenance",
      "the maintainers' perception that they are working without support",
      "pressure during maintenance activities to produce quantity, not quality".

   The paper does not seem to explicitly define criteria for software quality. But one might say that the authors
   would support a 'maintainability' criterion which measures the ease of carrying out maintenance activities without
   introducing new bugs. They mention logically complex code as being difficult to maintain, in particular in the
   absence of (correct) documentation.


---

## 146 - Quantitative evaluation of software quality

### Boehm B.W., Brown J.R., Lipow M.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-85042377749&partnerID=40&md5=86df793c94725cf352a0b8b3d8227c3c

The study reported in this paper establishes a conceptual framework and some key initial results in the analysis of the characteristics of software quality. Its main results and conclusions are: • Explicit attention to characteristics of software quality can lead to significant savings in software life-cycle costs. • The current software state-of-the-art imposes specific limitations on our ability to automatically and quantitatively evaluate the quality of software. • A definitive hierarchy of well-defined, well-differentiated characteristics of software quality is developed. Its higher-level structure reflects the actual uses to which software quality evaluation would be put; its lower-level characteristics are closely correlated with actual software metric evaluations which can be performed. • A large number of software quality-evaluation metrics have been defined, classified, and evaluated with respect to their potential benefits, quantifiability, and ease of automation. • Particular software life-cycle activities have been identified which have significant leverage on software quality. Most importantly, we believe that the study reported in this paper provides for the first time a clear, well-defined framework for assessing the often slippery issues associated with software quality, via the consistent and mutually supportive sets of definitions, distinctions, guidelines, and experiences cited. This framework is certainly not complete, but it has been brought to a point sufficient to serve as a viable basis for future refinements and extensions. © 1976 IEEE Computer Society. All rights reserved.

| MD  | ER  | MC  | VL  | DG  |
| --- | --- | --- | --- | --- |
| yes |     | yes | yes | yes |

### Review

| Paper_id | Name  | Definition | Qualitative/Quantitative | Targeted to SW | Reviewer  | Comment |
| :------: | :---: | :--------: | :----------------------: | :------------: | :-------: | :-----: |
| 146      |       |            |                          |                | VL        |         |

---

# To be discussed - mixed voting **yes + no** and **yes + no + unsure** - Total 28 articles

---

## 3 - The sustainability of quality in free and open source software

### Alami A.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-85094174322&doi=10.1145%2f3377812.3381402&partnerID=40&md5=afb03b21ee1d83333f142cfdf9d75b14

We learned from the history of software that great software are theones who manage to sustain their quality. Free and open sourcesoftware (FOSS) has become a serious software supply channel.However, trust on FOSS products is still an issue. Quality is a traitthat enhances trust. In my study, I investigate the following question: how do FOSS communities sustain their software quality? Iargue that human and social factors contribute to the sustainabilityof quality in FOSS communities. Amongst these factors are: themotivation of participants, robust governance style for the software change process, and the exercise of good practices in the pullrequests evaluation process. © 2020 Copyright held by the owner/author(s).

| MD  | ER     | MC  | VL  | DG  | JC  | MV  |
| --- | ------ | --- | --- | --- | --- | --- |
| no  | unsure |     | yes | no  | no  | yes |

* *ER* - this paper seems to be related to software development process. However it talks about sustainability factor and this could be one of the software dimention characteristics.
* *MD* - this seems to be about subjective factors, thus my vote

---

## 7 - How does developer interaction relate to software quality? an examination of product development data

### Datta S.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-85026823677&doi=10.1007%2fs10664-017-9534-0&partnerID=40&md5=1bcbb3493632b82239aeb55703852b5f

Industrial software systems are being increasingly developed by large and distributed teams. Tools like collaborative development environments (CDE) are used to facilitate interaction between members of such teams, with the expectation that social factors around the interaction would facilitate team functioning. In this paper, we first identify typically social characteristics of interaction in a software development team: reachability, connection, association, and clustering. We then examine how these factors relate to the quality of software produced by a team, in terms of the number of defects, through an empirical study of 70+ teams, involving 900+ developers in total, spread across 30+ locations and 19 time-zones, working on 40,000+ units of work in the multi-version development of a major industrial product, spreading across more than five years. After controlling for known factors affecting large scale distributed development such as dependency, system age, developer expertise and experience, geographic dispersion, socio-technical congruence, and the number of files changed, we find statistically significant effects of connection and clustering on software quality. Higher levels of intra-team connection are found to relate to higher defect count, whereas more clustering relates to fewer defects. We examine the implications of these results for individual developers, project managers, and organizations. © 2017, Springer Science+Business Media, LLC.

| MD  | ER  | MC  | VL  | DG  | JC  | MV  |
| --- | --- | --- | --- | --- | --- | --- |
| no  | no  | yes | yes | yes | no  | no  |

* *DG* - I think that this paper explores the social dimension of software quality, and it may define interesting aspects.
* *ER* - This is related to software development process
* *MC* - Related to Perspectives and Lanscaping too.
* *MD* - this seems to be about subjective factors, thus my vote

---

## 9 - Integrating software quality models into risk-based testing

### Foidl H., Felderer M.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-84994719172&doi=10.1007%2fs11219-016-9345-3&partnerID=40&md5=08aef64094ee176e3efa77d89641d4fa

Risk-based testing is a frequently used testing approach which utilizes identified risks of a software system to provide decision support in all phases of the testing process. Risk assessment, which is a core activity of every risk-based testing process, is often done in an ad hoc manual way. Software quality assessments, based on quality models, already describe the product-related risks of a whole software product and provide objective and automation-supported assessments. But so far, quality models have not been applied for risk assessment and risk-based testing in a systematic way. This article tries to fill this gap and investigates how the information and data of a quality assessment based on the open quality model QuaMoCo can be integrated into risk-based testing. We first present two generic approaches showing how quality assessments based on quality models can be integrated into risk-based testing and then provide the concrete integration on the basis of the open quality model QuaMoCo. Based on five open source products, a case study is performed. Results of the case study show that a risk-based testing strategy outperforms a lines of code-based testing strategy with regard to the number of defects detected. Moreover, a significant positive relationship between the risk coefficient and the associated number of defects was found. © 2016, The Author(s).

| MD  | ER  | MC  | VL  | DG  | JC  | MV  |
| --- | --- | --- | --- | --- | --- | --- |
|     | yes |     | no  | no  | no  | no  |

* *DG* -: This paper integrates existing quality models, but does not seem to define one. However, the referenced models could be used.

---

## 13 - A critical review of "a practical guide to select quality indicators for assessing pareto-based search algorithms in search-based software engineering": Essay on quality indicator selection for SBSE

### Li M., Chen T., Yao X.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-85049805170&doi=10.1145%2f3183399.3183405&partnerID=40&md5=cf1c999ddeb3da395195f2ba42440d27

This paper presents a critical review of the work published at ICSE'2016 on a practical guide of quality indicator selection for assessing multiobjective solution sets in search-based software engineering (SBSE). This review has two goals. First, we aim at explaining why we disagree with the work at ICSE'2016 and why the reasons behind this disagreement are important to the SBSE community. Second, we aim at providing a more clarified guide of quality indicator selection, serving as a new direction on this particular topic for the SBSE community. In particular, we argue that it does matter which quality indicator to select, whatever in the same quality category or across different categories. This claim is based upon the fundamental goal of multiobjective optimisation-supplying the decision-maker a set of solutions which are the most consistent with their preferences. © 2018 Association for Computing Machinery.

| MD  | ER     | MC  | VL  | DG  | JC  | MV     |
| --- | ------ | --- | --- | --- | --- | ------ |
|     | unsure |     | no  | yes | yes | unsure |

* *DG* - While a criticism, this paper defines quality indicators.
* *ER* - the abstract is quite general. It introduces the concept of quality indicator without introducing them.
* *JC* - Could include quality indicators

---

## 15 - Impact of customization over software quality in ERP projects: an empirical study

### Parthasarathy S., Sharma S.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-84964057687&doi=10.1007%2fs11219-016-9314-x&partnerID=40&md5=bbbd3a489ccce59d7785bbfd59804021

Enterprise resource planning (ERP) systems are recognized as management information systems that streamline business processes of an enterprise. Delivering ERP software to meet functional needs of an organization with acceptable level of quality is a challenge due to the very nature of development and deployment of this packaged software. Drawing on ISO/IEC 9126’s characterization of software quality and Luo and Strong’s ERP customization framework, this paper analyzes the impact of the ERP system customization on software quality of ERP. A software quality framework for ERP customization has been developed, and three sets of hypotheses have been formulated. A detailed survey was conducted for data collection. The statistical data analysis reveals that module customization does not impact ERP quality, while database and source code customizations have significant influence over ERP quality. Our findings have implications for the implementation of customized ERP in organizations. © 2016, Springer Science+Business Media New York.

| MD  | ER  | MC  | VL  | DG  | JC  | MV  |
| --- | --- | --- | --- | --- | --- | --- |
|     | no  | yes | no  | yes | yes | yes |

* *JC* - Includes definition of software quality
* *MC* - it might be useful to identify quality criteria specific to certain type of SW.

---

## 19 - An empirical study of the impact of modern code review practices on software quality

### McIntosh S., Kamei Y., Adams B., Hassan A.E.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-84928384936&doi=10.1007%2fs10664-015-9381-9&partnerID=40&md5=4ccadde0c9552d2747cfa6bdf80ff3ca

Software code review, i.e., the practice of having other team members critique changes to a software system, is a well-established best practice in both open source and proprietary software domains. Prior work has shown that formal code inspections tend to improve the quality of delivered software. However, the formal code inspection process mandates strict review criteria (e.g., in-person meetings and reviewer checklists) to ensure a base level of review quality, while the modern, lightweight code reviewing process does not. Although recent work explores the modern code review process, little is known about the relationship between modern code review practices and long-term software quality. Hence, in this paper, we study the relationship between post-release defects (a popular proxy for long-term software quality) and: (1) code review coverage, i.e., the proportion of changes that have been code reviewed, (2) code review participation, i.e., the degree of reviewer involvement in the code review process, and (3) code reviewer expertise, i.e., the level of domain-specific expertise of the code reviewers. Through a case study of the Qt, VTK, and ITK projects, we find that code review coverage, participation, and expertise share a significant link with software quality. Hence, our results empirically confirm the intuition that poorly-reviewed code has a negative impact on software quality in large systems using modern reviewing tools. © 2015, Springer Science+Business Media New York.

| MD  | ER  | MC  | VL  | DG  | JC  | MV  |
| --- | --- | --- | --- | --- | --- | --- |
| no  | no  | no  | yes | no  | no  | yes |

* *MC* - I don't expect this article to be useful to establish a definition of quality or general best practices.
* *MD* - seems only about code review, does not seems to add more than that.

---

## 21 - Improving and balancing software qualities

### Boehm B.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-85026633467&doi=10.1145%2f2889160.2891049&partnerID=40&md5=6d99ef500aabca2de5eabfb37df2b2d4

This Technical Briefing describes the nature of Software Qualities (SQs), ilities, or non-functional requirements (reliability, usability, affordability, etc.), and discusses the importance of understanding their nature and interrelationships, and of bringing them into balance in the practice of software engineering. The relevance and timeliness of this topic reflects the current and future trends toward more software-intensive systems, with greater complexity, autonomy, speed of change, and need for interoperability within systems of systems, given the frequent system shortfalls and overruns that occur when their SQ balance is not achieved. It discusses the weaknesses of current SQ standards and guidance, and summarizes research toward strengthening current SQ definitions and relationships. This includes a set of initial SQ ontology elements and relationships, examples of their application to some key SQs, an identification of further research and development needed to make the ontology fully useful and evolvable, and the nature of an international collaborative effort to help improve current practices via a Qualipedia for accessing the evolving body of knowledge for improving SQ engineering. © 2016 Author.

| MD  | ER         | MC  | VL  | DG  |
| --- | ---------- | --- | --- | --- |
| no  | unsure/yes | no  |     | yes |

* *ER* - useful for describing the problem, software characteristics
* *DG* - I think it defines non functional requirements for software quality that we may want to include in our work.

---

## 28 - Why good developers write bad code: An observational case study of the impacts of organizational factors on software quality

### Lavallée M., Robillard P.N.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-84951838553&doi=10.1109%2fICSE.2015.83&partnerID=40&md5=010ff95af592509e0c365f250fa510c3

How can organizational factors such as structure and culture have an impact on the working conditions of developers? This study is based on ten months of observation of an in-house software development project within a large telecommunications company. The observation was conducted during mandatory weekly status meetings, where technical and managerial issues were raised and discussed. Preliminary results show that many decisions made under the pressure of certain organizational factors negatively affected software quality. This paper describes cases depicting the complexity of organizational factors and reports on ten issues that have had a negative impact on quality, followed by suggested avenues for corrective action. © 2015 IEEE.

| MD  | ER  | MC  | VL  | DG  |
| --- | --- | --- | --- | --- |
| no  | yes | yes |     | no  |

* *ER* - useful for explaining negative impact on quality
* *MD* - although I voted no we should discuss
* *MC* - it's different point of view, focusing on the organizations. It might be useful when discussing in our report the best practices or how to implement the quality criteria.
* *DG* - I think this explores more a social problem

---

## 34 - Introduction of static quality analysis in small- and medium-sized software enterprises: experiences from technology transfer

### Gleirscher M., Golubitskiy D., Irlbeck M., Wagner S.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-84927804487&doi=10.1007%2fs11219-013-9217-z&partnerID=40&md5=96b5166ac6f386a4db36845b014b836d

Today, small- and medium-sized enterprises (SMEs) in the software industry face major challenges. Their resource constraints require high efficiency in development. Furthermore, quality assurance (QA) measures need to be taken to mitigate the risk of additional, expensive effort for bug fixes or compensations. Automated static analysis (ASA) can reduce this risk because it promises low application effort. SMEs seem to take little advantage of this opportunity. Instead, they still mainly rely on the dynamic analysis approach of software testing. In this article, we report on our experiences from a technology transfer project. Our aim was to evaluate the results static analysis can provide for SMEs as well as the problems that occur when introducing and using static analysis in SMEs. We analysed five software projects from five collaborating SMEs using three different ASA techniques: code clone detection, bug pattern detection and architecture conformance analysis. Following the analysis, we applied a quality model to aggregate and evaluate the results. Our study shows that the effort required to introduce ASA techniques in SMEs is small (mostly below one person-hour each). Furthermore, we encountered only few technical problems. By means of the analyses, we could detect multiple defects in production code. The participating companies perceived the analysis results to be a helpful addition to their current QA and will include the analyses in their QA process. With the help of the Quamoco quality model, we could efficiently aggregate and rate static analysis results. However, we also encountered a partial mismatch with the opinions of the SMEs. We conclude that ASA and quality models can be a valuable and affordable addition to the QA process of SMEs. © Springer Science+Business Media New York 2013.

| MD  | ER  | MC  | VL  | DG  |
| --- | --- | --- | --- | --- |
| yes |     | yes |     | no  |

* *MC* - related to SW in prod.
* *DG* - I think they apply a quality model (which we may review), but the paper does not define quality dimensions 

---

## 36 - New perspectives on software quality

### Breu R., Kuntzmann-Combelles A., Felderer M.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-84896288088&doi=10.1109%2fMS.2014.9&partnerID=40&md5=6e2e5fb2f50c47f1203ae65ab9be581d

This special issue, owing to its fundamental software quality focus, comprises a collection of diverse articles that address the challenges and directions for software quality research. The Web extra at http://youtu.be/ T7V4RSr1KEE is an audio interview in which Davide Falessi speaks with guest editors Annie Kuntzmann-Combelles, Michael Felderer, and Ruth Breu about methods for improving software quality management, testing, and security on intelligent and interconnected devices. © 1984-2012 IEEE.

| MD  | ER     | MC  | VL  | DG  |
| --- | ------ | --- | --- | --- |
| no  | unsure | no  |     | yes |

* *ER* - useful for new challenges for software quality research
* *DG* - I agree
* *MC* - I think it's better to focus on published peer-review material. Even though this interview might provide interesting insights, I wouldn't consider it.

---

## 39 - MIDAS: A design quality assessment method for industrial software

### Samarthyam G., Suryanarayana G., Sharma T., Gupta S.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-84886396370&doi=10.1109%2fICSE.2013.6606640&partnerID=40&md5=ad0d81ee2973d5ee478e587bb1b55aa5

Siemens Corporate Development Center Asia Australia (CT DC AA) develops and maintains software applications for the Industry, Energy, Healthcare, and Infrastructure & Cities sectors of Siemens. The critical nature of these applications necessitates a high level of software design quality. A survey of software architects indicated a low level of satisfaction with existing design assessment practices in CT DC AA and highlighted several shortcomings of existing practices. To address this, we have developed a design assessment method called MIDAS (Method for Intensive Design ASsessments). MIDAS is an expert-based method wherein manual assessment of design quality by experts is directed by the systematic application of design analysis tools through the use of a three view-model consisting of design principles, project-specific constraints, and an 'ility'-based quality model. In this paper, we describe the motivation for MIDAS, its design, and its application to three projects in CT DC AA. We believe that the insights from our MIDAS experience not only provide useful pointers to other organizations and practitioners looking to assess and improve software design quality but also suggest research questions for the software engineering community to explore. © 2013 IEEE.

| MD  | ER  | MC  | VL  | DG  |
| --- | --- | --- | --- | --- |
| no  |     |     |     | yes |

* *DG* - A quality model is proposed.

---

## 47 - Strategy to improve quality for software applications: A process view

### Becker P., Lew P., Olsina L.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-79960589413&doi=10.1145%2f1987875.1987897&partnerID=40&md5=697727eaef77cbebdc3618cbb98affc8

Each organization devoted to developing software/web applications should have as one of its ultimate goals to improve the quality in use of its products. In order to accomplish this, first it has to understand the quality of the current product version and then make appropriate changes to increase the quality of the new version if improvement actions were needed. For this purpose, we have developed a specific strategy called SIQinU (Strategy for understanding and Improving Quality in Use), which allows recognizing problems of quality in use through evaluation and proposes product improvements by understanding and making changes on product attributes. Hence by re-evaluating quality in use of the new version, improvement gains can be gauged. SIQinU is in alignment with GOCAME (Goal-Oriented Context-Aware Measurement and Evaluation), a multi-purpose generic strategy previously developed for measurement and evaluation which relies on: a conceptual framework (with ontological base), a process, and methods and tools. Since the process aspect is paramount in defining SIQinU - given the amount of phases and activities - in this paper we model the functional and behavioral process views illustrating them with excerpts of a real case study. © 2011 ACM.

| MD     | ER  | MC  | VL  | DG  |
| ------ | --- | --- | --- | --- |
| unsure |     | no  |     | yes |

* *DG* - It has a methodological view that may be useful for quality definition

---

## 50 - Pragmatic prioritization of software quality assurance efforts

### Shihab E.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-79959864680&doi=10.1145%2f1985793.1986007&partnerID=40&md5=0e2ecdae077441ec1422a8aaa4bbf673

A plethora of recent work leverages historical data to help practitioners better prioritize their software quality assurance efforts. However, the adoption of this prior work in practice remains low. In our work, we identify a set of challenges that need to be addressed to make previous work on quality assurance prioritization more pragmatic. We outline four guidelines that address these challenges to make prior work on software quality assurance more pragmatic: 1) Focused Granularity (i.e., small prioritization units), 2) Timely Feedback (i.e., results can be acted on in a timely fashion), 3) Estimate Effort (i.e., estimate the time it will take to complete tasks), and 4) Evaluate Generality (i.e., evaluate findings across multiple projects and multiple domains). We present two approaches, at the code and change level, that demonstrate how prior approaches can be more pragmatic. © 2011 Author.

| MD         | ER  | MC     | VL  | DG     |
| ---------- | --- | ------ | --- | ------ |
| yes/unsure |     | unsure |     | unsure |

---

## 53 - A framework for evaluating quality-driven self-adaptive software systems

### Villegas N.M., Müller H.A., Tamura G., Duchien L., Casallas R.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-79959550156&doi=10.1145%2f1988008.1988020&partnerID=40&md5=87328f5539e05de7c67c753109f03509

Over the past decade the dynamic capabilities of self-adaptive software-intensive systems have proliferated and improved significantly. To advance the field of self-adaptive and self-managing systems further and to leverage the benefits of self-adaptation, we need to develop methods and tools to assess and possibly certify adaptation properties of self-adaptive systems, not only at design time but also, and especially, at run-time. In this paper we propose a framework for evaluating quality-driven self-adaptive software systems. Our framework is based on a survey of self-adaptive system papers and a set of adaptation properties derived from control theory properties. We also establish a mapping between these properties and software quality attributes. Thus, corresponding software quality metrics can then be used to assess adaptation properties. © 2011 ACM.

| MD     | ER  | MC  | VL  | DG  |
| ------ | --- | --- | --- | --- |
| unsure |     | no  |     | yes |

---

## 63 - Software aging assessment through a specialization of the SQuaRE quality model

### Bombardieri M., Fontana F.A.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-78049458138&doi=10.1109%2fWOSQ.2009.5071554&partnerID=40&md5=3085a2d9022674d883b077f87722de88

In the last years the software application portfolio has become a key asset for almost all companies. During their lives, applications undergo lots of changes to add new functionalities or to refactor older ones; these changes tend to reduce the quality of the applications themselves, causing the phenomenon known as software aging. Monitoring of software aging is very important for companies, but up to now there are no standard approaches to perform this task. In addition many of the suggested models assess software aging basing on few software features, whereas this phenomenon affects all of the software aspects. In 2005 ISO/IEC released the SQuaRE quality model which covers several elements of software quality assessment, but some issues make SQuaRE usage quite difficult. The purpose of this paper is to suggest an approach to software aging monitoring that considers the software product in its wholeness and to provide a specialization of the SQuaRE quality model which allows to perform this task. © 2009 IEEE.

| MD         | ER  | MC  | VL  | DG  |
| ---------- | --- | --- | --- | --- |
| yes/unsure |     | yes |     | no  |

* *MD* - provide a specialization of the SQuaRE quality model
* *MC* - totally related to SW maintainabily and SW in production.
* *DG* - We should include SQuaRE, but not this one (i think)

---

## 64 - Inspection effectiveness for different quality attributes of software requirement specifications: An industrial case study

### Salger F., Engels G., Hofmann A.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-77955167159&doi=10.1109%2fWOSQ.2009.5071552&partnerID=40&md5=6f5d87e6b9a0e8abe8256ba0756f9df0

Early inspections of software requirements specifications (SRS) are known to be an effective and cost-efficient quality assurance technique. However, inspections are often applied with the underlying assumption that they work equally well to assess all kinds of quality attributes of SRS. Little work has yet been done to validate this assumption. At Capgemini sd&m, we set up an inspection technique to assess SRS, the so called "specification quality gate" (QG-Spec). The QG-Spec has been applied to a series of large scale commercial projects. In this paper we present our lessons learned and discuss, which quality attributes are effectively assessed by means of the QG-Spec - and which are not. We argue that our results can be generalized to other existing inspection techniques. We came to the conclusion that inspections have to be carefully balanced with techniques for constructive quality assurance in order to economically arrive at high quality SRS. © 2009 IEEE.

| MD  | ER  | MC     | VL  | DG  |
| --- | --- | ------ | --- | --- |
| yes |     | unsure |     | no  |

* *MD* - quality attributes
* *MC*: it seems from the abtract that the authors propose a more general evaluation framework which englobes SRS, to take into account economical considerations. I see it's useful, but probably it's not directly related to SW quality, but to making compromises. 
* *DG* - The focus is on software requirement specification, not software quality

---

## 67 - Improving Software quality via code searching and mining

### Marri M.R., Thummalapenta S., Xie T.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-77949788600&doi=10.1109%2fSUITE.2009.5070018&partnerID=40&md5=ad93b9e9acb8a8992d77216d08a24c2d

Enormous amount of open source code is available on the Internet and various code search engines (CSE) are available to serve as a means for searching in open source code. However, usage of CSEs is often limited to simple tasks such as searching for relevant code examples. In this paper, we present a generic life-cycle model that can be used to improve software quality by exploiting CSEs. We present three example software development tasks that can be assisted by our life-cycle model and show how these three tasks can contribute to improve the software quality. We also show the application of our life-cycle model with a preliminary evaluation. © 2009 IEEE.

| MD         | ER  | MC     | VL  | DG     |
| ---------- | --- | ------ | --- | ------ |
| yes/unsure |     | unsure |     | unsure |

* *MD* - software development tasks,... three tasks can contribute to improve the software quality

---

## 72 - Should we try to measure software quality attributes directly?

### Moses J.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-64249172602&doi=10.1007%2fs11219-008-9071-6&partnerID=40&md5=0648b6d6e222796c2e98f7d73d843380

Most external software quality attributes are conceptually subjective. For example, maintainability is an external software quality attribute, and it is subjective because interpersonally agreed definitions for the attribute include the phrase 'the ease with which maintenance tasks can be performed'. Subjectivity clearly makes measurement of the attributes and validation of prediction systems for the attributes problematic. In fact, in spite of the definitions, few statistically valid attempts at determining the predictive capability of prediction systems for external quality attributes have been published. When validations have been attempted, one approach used is to ask experts to indicate if the values provided by the prediction system informally agree with the experts' intuition. These attempts are undertaken without determining, independently of the prediction system, whether the experts are capable of direct consistent measurement of the attribute. Hence, a statistically valid and unbiased estimate of the predictive capability of the prediction system cannot be obtained (because the experts' measurement process is not independent of the prediction system's values). In this paper, it is argued that the problem of subjective measurement of quality attributes should not be ignored if quality is to be introduced into software in a controlled way. Further, it is argued that direct measurement of quality attributes should be encouraged and that in fact such measurement can be quantified to establish consistency using an existing approach. However, the approach needs to be made more accessible to promote its use. In so doing, it would be possible to decide whether consistent independent estimates of the true values of software quality attributes can be assigned and prediction systems for quality attributes developed. © 2009 Springer Science+Business Media, LLC.

| MD  | ER  | MC  | VL  | DG     |
| --- | --- | --- | --- | ------ |
| yes | yes | no  |     | unsure |

* *ER* - software characteristics
* *MC* - I'm not sure if "subjective" quality assessment is useful for our definition purposes.

---

## 79 - Engineering models and software quality models: An example and a discussion

### Salvaneschi P., Piazzalunga U.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-79959190479&doi=10.1145%2f1370731.1370741&partnerID=40&md5=d2ce735f0f93bb485210c6ccb9125006

The paper compares the models used for software quality evaluation to the modelling approach of other engineering fields. The conclusion is that, while large efforts have been devoted to the definition of measurable attributes and related measures, product models specifically developed for measuring quality characteristics are until now not sufficiently explored. We explore the concept of "quality-oriented specialized product models" and we claim that this is an important ingredient for an engineering approach to the software quality measurement. We describe an example of this type of models for measuring the security of a specific type of copy protection mechanisms. The model forecasts the amount of time a hypothetical attacker would need to break the protection. Copyright 2008 ACM.

| MD  | ER  | MC  | VL  | DG  |
| --- | --- | --- | --- | --- |
| no  |     |     |     | yes |

* *DG* - I think the comparison may emphasize quality dimensions that could be interesting to include.

---

## 91 - The software quality challenges of service oriented architectures in e-commerce

### Saunders S., Ross M., Staples G., Wellington S.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-33244469280&doi=10.1007%2fs11219-006-6002-2&partnerID=40&md5=4a75561cafd69887db2378a084af2ed1

Web Services technologies and their supporting collection of de facto standards are now reaching the point of maturity where they are appearing in production software systems. Service Oriented Architectures (SOAs) using Web Services as an enabling technology are also being discussed widely in the IT press. However, despite the numerous and real advantages of these architectural patterns there are still many software quality challenges that remain unresolved. This is particularly true as we consider more advanced architectures that exploit the technology to its maximum advantage: utility computing and on-demand service discovery and composition, grid computing and multi-agent systems will only become pervasive once the software quality challenges of real-world industrial applications have been addressed. In this paper potential quality issues such as performance, reliability and availability are addressed in terms of the quality assurances that might need to be provided to consumers of services. Proposed XML-based Service Level Agreement (SLA) languages are reviewed as a means of providing these quality assurances in machine-readable ways. We also discuss how SLAs might be automatically negotiated to enable automated, on-demand service discovery and composition. The next section of this paper addresses quality issues from a service provider's perspective. The providers of such services will need to ensure that SLA commitments are met and this poses interesting problems in terms of application management. Network quality of service is currently addressed through such means as IntServ and DiffServ. Research proposals to introduce similar techniques at an application level are described. From the service consumer's perspective, interesting research proposals for proactively ensuring that good quality of service is obtained are also reviewed. These could be particularly important for creating confidence, from a consumer's perspective, in these architectures. Finally, the paper evaluates the challenges and suggests areas where further research is most urgently required. © Springer Science + Business Media, Inc. 2006.

| MD     | ER  | MC  | VL  | DG  |
| ------ | --- | --- | --- | --- |
| unsure |     | yes | no  |  no |

* *MC* - probably related to scalabily and data formats. Useful for Landscaping and SW in production.

---

## 94 - Improving scientific software component quality through assertions

### Dahlgren T.L., Devanbu P.T.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-77954433188&doi=10.1145%2f1145319.1145341&partnerID=40&md5=3e2d8e96ab9ab9d7e44210eba3b18e87

We are proposing research on self-adaptive interface assertion enforcement for the purposes of improving scientific software component quality. Demonstrating software correctness through assertions is a well-known technique for quality improvement. However, the performance penalty is often considered too high for deployment. In order to determine if partial enforcement based on adaptive sampling is a viable solution in performance critical environments, we are pursuing research on mechanisms combining static and dynamic analyses to efficiently maximize assertion checking within performance constraints. This paper gives an overview of our initial experiments, current work, and plans. Copyright 2005 ACM.

| MD  | ER  | MC  | VL     | DG  |
| --- | --- | --- | ------ | --- |
| yes |     | yes | unsure | no  |

* *MC* - assertions are general, but perhaps very important for research software. Useful for Landscaping.

---

## 107 - GEQUAMO - A generic, multilayered, customisable, software quality model

### Georgiadou E.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-3543133647&doi=10.1023%2fA%3a1025817312035&partnerID=40&md5=badb2f8c8a55653a96fec05d28815c48

Software quality models have primarily been based on top down process improvement approaches. Such models are based on the fundamental principle of empowerment of all involved and foster a questioning attitude through the active exchange of ideas and criticism ensuring that the most appropriate approach for quality improvements is adopted. The holistic view of systems enables the incorporation of many viewpoints held by different parties within the same organisation and by the same party at different stages of development. In this paper the GEQUAMO (GEneric, multilayered and customisable) QUAlity MOdel is proposed. GEQUAMO encapsulates the requirements of different stakeholders in a dynamic and flexible manner so as to enable each stakeholder (developer, user or sponsor) to construct their own model reflecting the emphasis/weighting for each attribute/requirement. Using a combination of the CFD (Composite Features Diagramming Technique) developed by the author, and Kiviat diagrams a multilayered and dynamic model is constructed. Instances of models are presented together with the algorithm for the computation of the profiles. Indications of future work conclude the paper.

| MD  | ER  | MC  | VL  | DG  |
| --- | --- | --- | --- | --- |
|     | no  |     |     | yes |

* *ER*: useful for building software quality model
* *DG* - It's defining a quality model, which is kind of what we need to review, don't we?

---

## 114 - Method for software quality planning, control, and evaluation

### Boegh Jorgen, Depanfilis Stefano, Kitchenham Barbara, Pasquini Alberto

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-0033097512&doi=10.1109%2f52.754056&partnerID=40&md5=97fc63f1814469a1306aed28d10729d6

An increasing number of software process and product standards emphasize the need for measurement. ISO 9001, for example, provides guidance for monitoring and controlling product and process characteristics during both production and installation. However, standards provide little guidance as to what exactly users should measure and how to use the results to support the development of high-quality software. Furthermore, measurement cannot be defined independent of context. A metric set judged valid on one project may lead to poor quality or high development costs when applied to another project. When quality is measured, several factors come into play, including product characteristics (such as size), process maturity level of the company developing the software product, its development environment (such as the design methodology and CASE tools used), and the development team's skill and experience.

| MD     | ER  | MC  | VL  | DG  |
| ------ | --- | --- | --- | --- |
| unsure |     | yes |     | no  |

* *MC* - I think it's worth it to have a look. They refer to "high-quality" SW, so I expect they give a definition.

---

## 119 - Efficiency of CAME tools in software quality assurance

### Dumke R.R., Grigoleit H.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-0642333260&doi=10.1023%2fA%3a1018507901618&partnerID=40&md5=0ce0041f30ceaef95ce87fd174655648

Our paper describes the requirements and possibilities of integration of metrics tools in the field of software quality assurance. Tools for the support of the measurement process are herein classified as Computer Assisted Software Measurement and Evaulation Tools (CAME Tools). Software measurement regarded as a special type of metrics application provides a great amount of basic information for the evaluation of the software development process or the software product itself. Our paper examines the effectiveness and destination of software measurement in tool-based software development and is based on an analysis of more than 20 CAME tools in the Software Measurement Laboratory at the University of Magdeburg. CAME tools are useable for the process, product, and resources evaluation in all phases of the software life cycle (including the problem definition) for different development paradigms. The efficiency of CAME tools is described on the basis of a general measurement framework. This framework includes all steps in the software measurement and evaulation process: metrics definition, selection of the evaluation criteria, tool-based modelling and measurement, value presentation and statistical analysis. The framework includes the main aspects of the process evaluation techniques (Capability Maturity Model, ISO 9000-3 etc.) and product evaluation (ISO 9126, etc.). It is not a disjointed set of aspects: our measurement framework represents an incremental technique for the application of quantification of quality aspects in a required quality assurance.

| MD     | ER  | MC  | VL  | DG  |
| ------ | --- | --- | --- | --- |
| unsure |     | yes |     | no  |

* *MC* - if the propose automatic evaluation with tools, they should provide some objective criteria.

---

## 126 - Frameworks for quality software process: SEI Capability maturity model versus ISO 9000

### Saiedian H., Mcclanahan L.M.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-0007663827&doi=10.1007%2fBF02420941&partnerID=40&md5=920d8525d6033e615724b4a8ab7ec770

With the historical characterization of software development as being costly due to massive schedule delays, incorporation of the ever-changing technology, budget reductions, and missing customer requirements, the trend of the 1990s in establishing a quality improvement or a quality assurance programme has been overwhelming. The two popular models or frameworks for assessment of a quality assurance programme are the US government-sponsored Capability Maturity Model (CMM) and the internationally recognized ISO-9000 quality standards. Both of these two frameworks share a common concern regarding software quality and process management. Since it is not clear which of these two frameworks is most effective in achieving their shared objectives, it is valuable and timely to provide an objective overview of both models and to compare and contrast their features for quality software development. Because there are many legitimate areas for comparison, we have selected the two most important as a basis for comparison: (1) the role of management, and (2) the application of measurements. We also provide a summary of the reported impact of these two models on the organizations adhering to their standards, and include our observations and analysis. © 1996 Chapman & Hall.

| MD  | ER  | MC  | VL     | DG  |
| --- | --- | --- | ------ | --- |
|     |     | no  | unsure | yes |

* *MC* - it looks more about organizational aspects than quality itself.
* *DG* - Comparison between 2 quality models

---

## 127 - Factors affecting the quality of software project management:an empirical study based on the Capability Maturity Model

### Mcguire E.G.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-0007176737&doi=10.1007%2fBF00209188&partnerID=40&md5=8a9f2fa4e39735762608ce94c38112e4

Rigorous project management can help raise a software product development process from an initial, immature stage that is unstable and unrepeatable to an optimized maturity level characterized by continuous improvement and innovation. Goals and actions related to a repeatable project management process have been outlined in the Capability Maturity Model (CMM) developed by the Software Engineering Institute at Carnegie Mellon University. The CMM provides good guidelines for initiating software process improvement particularly in the project management area; however, the successful implementation of the CMM guidelines is often not accomplished without significant organizational change involving increased emphasis on change management, teams and employee empowerment. This paper is empirically based on observations, surveys, and interviews of project team managers and project team members in a large, multinational organization. The focus of the paper is on the development of a project management process that emphasizes project planning, change management, quality management, team work, and process control. Findings presented in this paper are correlated with the CMM guidelines as well as organizational factors that were found to enable or impede the successful deployment of various aspects of a project management improvement plan. The role of education and training in process and quality techniques as well as project management tools that support group work is also examined. This paper provides some insight into the issues faced by organizations based on traditional hierarchy or matrix management as they attempt to move into a more process-driven, quality-oriented development environment. As organizations move towards global markets they need increased emphasis on quality, value, teams, standards and global project management strategies based on structured guidelines to handle process Sow within and between projects, departments, organizations, and national boundaries. © 1996 Chapman & Hall.

| MD  | ER  | MC  | VL  | DG     |
| --- | --- | --- | --- | ------ |
|     |     | no  | yes | unsure |

* *MC* - I don't think they're discussing the same quality concept we're working on.
* *DG* - The paper seems focused on quality management of software. However, the dimensions used could be helpful

---

## 139 - Software process maturity: measuring its impact on productivity and quality

### Rubin Howard A.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-0027150237&doi=10.1109%2fICSE.1993.346019&partnerID=40&md5=8d9c01a05ed505732258e69067392a1f

With the current worldwide focus on improvement in software process, there is clearly a need for an understanding of its impact on software engineering productivity and quality. This paper documents an attempt to provide an empirical metrics ″view″ of such initiatives based on data collected in a worldwide benchmarking effort conducted between March, 1991 and December, 1991. Surprisingly, of the more than 300 organizations that participated, fewer than 1 in 5 had any quantifiable performance data available prior to the start of this study. However, those that had embarked on significant process improvement efforts and were actively using metrics were able to demonstrate substantial gains in productivity and quality. In addition, insights derived from this large scale data analysis provide a framework for determining which metrics should be included in a standard software engineering measurement 'dashboard'.

| MD  | ER  | MC  | VL     | DG  |
| --- | --- | --- | ------ | --- |
|     |     | yes | unsure | no  |

* *MC* - if it's about 'measuring' then it should provide objective criteria.

---

## 141 - On specifying software quality

### Dromey R.G., McGettrick A.D.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-0008302517&doi=10.1007%2fBF01720169&partnerID=40&md5=f297222c53ba1b94f0ae36ebdd761820

Quality is recognized as a pre-eminently important characteristic of software, yet an understanding of how to usefully define it, and how to achieve it remains illusive. A constructive definition of quality is investigated and an approach to the construction of software of quality is suggested. The definition focusses on how well the solution fits the problem, the inherent quality of the design independent of the problem, and the quality of the design process that creates the solution. A constructive specification of software quality then follows based on the use of programming language syntax, design principles and strategies, post-construction program quality analysis systems, and computer-assisted program construction tools. Only by addressing the problem on much broader methodological, technical, and managerial fronts will it be possible to make significant gains in software quality. © 1992 Chapman & Hall.

| MD  | ER  | MC  | VL  | DG  |
| --- | --- | --- | --- | --- |
| yes | no  | no  | yes | yes |

* *ER* - the same author wrote the article [A model for software product quality, 1995](https://ieeexplore.ieee.org/document/345830). There is also [Security quality model: an extension of Dromey’s model, 2015](https://link.springer.com/article/10.1007/s11219-013-9223-1) 
* *MC* - in that case, let's consider the 1995's article, which seems absolutely useful for our task.
* *DG* - We should probably pick one of them (1995 model, perhaps?)

---

# Selected with **no** and **no + unsure** - Total 28 articles

---

## 16 - Productivity paradoxes revisited: Assessing the relationship between quality maturity levels and labor productivity in brazilian software companies

### C. Duarte C.H.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-84989910841&doi=10.1007%2fs10664-016-9453-5&partnerID=40&md5=c4582eabccfbbf9c77fc764b7dd8fa00

The adoption of quality assurance methods based on software process improvement models has been regarded as an important source of variability in software productivity. Some companies perceive that their implementation has prohibitive costs, whereas some authors identify in their use a way to comply with software development patterns and standards, produce economic value and lead to corporate performance improvement. In this paper, we investigate the relationship between quality maturity levels and labor productivity, using a data set containing 687 Brazilian software firms. We study here the relationship between labor productivity, as measured through the annual gross revenue per worker ratio, and quality levels, which were appraised from 2006 to 2012 according to two distinct software process improvement models: MPS.BR and CMMI. We perform independent statistical tests using appraisals carried out according to each of these models, consequently obtaining a data set with as many observations as possible, in order to seek strong support for our research. We first show that MPS.BR and CMMI appraised quality maturity levels are correlated, but we find no statistical evidence that they are related to higher labor productivity or productivity growth. On the contrary, we present evidence suggesting that average labor productivity is higher in software companies without appraised quality levels. Moreover, our analyses suggest that companies with appraised quality maturity levels are more or less productive depending on factors such as their business nature, main origin of capital and maintained quality level. © 2016, Springer Science+Business Media New York.

| MD  | ER  | MC  | VL  | DG     | JC  | MV  |
| --- | --- | --- | --- | ------ | --- | --- |
|     | no  |     | no  | unsure | no  | no  |

* *DG*- This seems to be a comparison among existing models.
* *MC* - related to quality, but it seems the focus is on productivity.

---

## 18 - On the use of many quality attributes for software refactoring: a many-objective search-based software engineering approach

### Mkaouer M.W., Kessentini M., Bechikh S., Ó Cinnéide M., Deb K.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-84951756385&doi=10.1007%2fs10664-015-9414-4&partnerID=40&md5=9b6ecf0a25cc8eb003e321aff9f5b63c

Search-based software engineering (SBSE) solutions are still not scalable enough to handle high-dimensional objectives space. The majority of existing work treats software engineering problems from a single or bi-objective point of view, where the main goal is to maximize or minimize one or two objectives. However, most software engineering problems are naturally complex in which many conflicting objectives need to be optimized. Software refactoring is one of these problems involving finding a compromise between several quality attributes to improve the quality of the system while preserving the behavior. To this end, we propose a novel representation of the refactoring problem as a many-objective one where every quality attribute to improve is considered as an independent objective to be optimized. In our approach based on the recent NSGA-III algorithm, the refactoring solutions are evaluated using a set of 8 distinct objectives. We evaluated this approach on one industrial project and seven open source systems. We compared our findings to: several other many-objective techniques (IBEA, MOEA/D, GrEA, and DBEA-Eps), an existing multi-objective approach a mono-objective technique and an existing refactoring technique not based on heuristic search. Statistical analysis of our experiments over 31 runs shows the efficiency of our approach. © 2015, Springer Science+Business Media New York.

| MD  | ER  | MC  | VL  | DG  | JC  | MV     |
| --- | --- | --- | --- | --- | --- | ------ |
|     | no  |     | no  | no  | no  | unsure |

* *MV* - Also this one could include quality indicators

---

## 20 - Software quality improvement: a model based on managing factors impacting software quality

### Janicijevic I., Krsmanovic M., Zivkovic N., Lazarevic S.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-84908118810&doi=10.1007%2fs11219-014-9257-z&partnerID=40&md5=49441ef38876a3665b52cb6086473831

Software quality is recognized as being very significant for achieving competitiveness in the software industry, so improvements in this area are gaining increasing importance. Software quality improvements can only be achieved by managing all of the factors that influence it. However, in a real business system, there are a great number of factors impacting software quality, while the processes are stochastic and resources are limited, so economic data should also be taken into consideration. This paper uses a Markov chain and proposes a systematic framework for modelling the stochastic processes of a quality management system and selection of the optimum set of factors impacting software quality. A methodology is presented for managing the factors that affect software quality with an illustrative hypothetical example for convenience of application of the proposed methodology. © 2014, Springer Science+Business Media New York.

| MD        | ER  | MC  | VL  | DG  |
| --------- | --- | --- | --- | --- |
| unsure/no |     | no  |     |     |

* *MC* - another example of paper about management of organization, and not that much about quality itself.

---

## 23 - Revisiting code ownership and its relationship with software quality in the scope of modern code review

### Thongtanunam P., McIntosh S., Hassan A.E., Iida H.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-84971482984&doi=10.1145%2f2884781.2884852&partnerID=40&md5=0c2da8fa587f2d260b605b676b5a2c31

Code ownership establishes a chain of responsibility for modules in large software systems. Although prior work uncovers a link between code ownership heuristics and software quality, these heuristics rely solely on the authorship of code changes. In addition to authoring code changes, developers also make important contributions to a module by reviewing code changes. Indeed, recent work shows that reviewers are highly active in modern code review processes, often suggesting alternative solutions or providing updates to the code changes. In this paper, we complement traditional code ownership heuristics using code review activity. Through a case study of six releases of the large Qt and OpenStack systems, we find that: (1) 67%-86% of developers did not author any code changes for a module, but still actively contributed by reviewing 21%-39% of the code changes, (2) code ownership heuristics that are aware of reviewing activity share a relationship with software quality, and (3) the proportion of reviewers without expertise shares a strong, increasing relationship with the likelihood of having post-release defects. Our results suggest that reviewing activity captures an important aspect of code ownership, and should be included in approximations of it in future studies. © 2016 ACM.

| MD     | ER  | MC  | VL  | DG  |
| ------ | --- | --- | --- | --- |
| unsure |     | no  |     | no  |

* *MC* - I don't think this study is useful to define what SW quality should be.

---

## 24 - A practical guide to select quality indicators for assessing pareto-based search algorithms in search-based software engineering

### Wang S., Ali S., Yue T., Li Y., Liaaen M.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-84971412816&doi=10.1145%2f2884781.2884880&partnerID=40&md5=fb106f940fea5f845deddb5ac287de81

Many software engineering problems are multi-objective in nature, which has been largely recognized by the Search-based Software Engineering (SBSE) community. In this regard, Paretobased search algorithms, e.g., Non-dominated Sorting Genetic Algorithm II, have already shown good performance for solving multi-objective optimization problems. These algorithms produce Pareto fronts, where each Pareto front consists of a set of nondominated solutions. Eventually, a user selects one or more of the solutions from a Pareto front for their specific problems. A key challenge of applying Pareto-based search algorithms is to select appropriate quality indicators, e.g., hypervolume, to assess the quality of Pareto fronts. Based on the results of an extended literature review, we found that the current literature and practice in SBSE lacks a practical guide for selecting quality indicators despite a large number of published SBSE works. In this direction, the paper presents a practical guide for the SBSE community to select quality indicators for assessing Pareto-based search algorithms in different software engineering contexts. The practical guide is derived from the following complementary theoretical and empirical methods: 1) key theoretical foundations of quality indicators; 2) evidence from an extended literature review; and 3) evidence collected from an extensive experiment that was conducted to evaluate eight quality indicators from four different categories with six Pareto-based search algorithms using three real industrial problems from two diverse domains. © 2016 ACM.

| MD        | ER     | MC  | VL  | DG  |
| --------- | ------ | --- | --- | --- |
| unsure/no | unsure | no  |     | no  |

* *ER* - software metrics
* *MC* - I'm not confident at all about this paper (too strong and surprising claims based on a very specific methodology), but if they provide quality indicators we can have a look.

---

## 35 - Quality attribute modeling and quality aware product configuration in software product lines

### Zhang G., Ye H., Lin Y.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-84875049200&doi=10.1007%2fs11219-013-9197-z&partnerID=40&md5=ad822ef7f6b285eb153f76658a503708

In software product line engineering, the customers mostly concentrate on the functionalities of the target product during product configuration. The quality attributes of a target product, such as security and performance, are often assessed until the final product is generated. However, it might be very costly to fix the problem if it is found that the generated product cannot satisfy the customers’ quality requirements. Although the quality of a generated product will be affected by all the life cycles of product development, feature-based product configuration is the first stage where the estimation or prediction of the quality attributes should be considered. As we know, the key issue of predicting the quality attributes for a product configured from feature models is to measure the interdependencies between functional features and quality attributes. The current existing approaches have several limitations on this issue, such as requiring real products for the measurement or involving domain experts’ efforts. To overcome these limitations, we propose a systematic approach of modeling quality attributes in feature models based on domain experts’ judgments using the analytic hierarchical process (AHP) and conducting quality aware product configuration based on the captured quality knowledge. Domain experts’ judgments are adapted to avoid generating the real products for quality evaluation, and AHP is used to reduce domain experts’ efforts involved in the judgments. A prototype tool is developed to implement the concepts of the proposed approach, and a formal evaluation is carried out based on a large-scale case study. © 2013, Springer Science+Business Media New York.

| MD        | ER  | MC  | VL  | DG     |
| --------- | --- | --- | --- | ------ |
| unsure/no |     | no  |     | unsure |

* *MC* - their concept of "quality" is too general ("security", "performance"), and it doesn't much our task.
* *DG* - The quality attributes defined may be useful

---

## 38 - Studying the effect of co-change dispersion on software quality

### Kouroshfar E.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-84886429987&doi=10.1109%2fICSE.2013.6606741&partnerID=40&md5=f9b5aa44f572315b1cd1c58858d1d1a6

Software change history plays an important role in measuring software quality and predicting defects. Co-change metrics such as number of files changed together has been used as a predictor of bugs. In this study, we further investigate the impact of specific characteristics of co-change dispersion on software quality. Using statistical regression models we show that co-changes that include files from different subsystems result in more bugs than co-changes that include files only from the same subsystem. This can be used to improve bug prediction models based on co-changes. © 2013 IEEE.

| MD     | ER  | MC  | VL  | DG  |
| ------ | --- | --- | --- | --- |
| unsure |     | no  |     | no  |

* *MC* - it seems their criteria of "quality" is the detection of bugs. I don't think this study is useful for us.

---

## 40 - Normalizing source code vocabulary to support program comprehension and software quality

### Guerrouj L.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-84886391532&doi=10.1109%2fICSE.2013.6606723&partnerID=40&md5=191e7233ea6777ff76ebefbf832bbda5

The literature reports that source code lexicon plays a paramount role in program comprehension, especially when software documentation is scarce, outdated or simply not available. In source code, a significant proportion of vocabulary can be either acronyms and-or abbreviations or concatenation of terms that can not be identified using consistent mechanisms such as naming conventions. It is, therefore, essential to disambiguate concepts conveyed by identifiers to support program comprehension and reap the full benefit of Information Retrieval-based techniques (e.g., feature location and traceability) whose linguistic information (i.e., source code identifiers and comments) used across all software artifacts (e.g., requirements, design, change requests, tests, and source code) must be consistent. To this aim, we propose source code vocabulary normalization approaches that exploit contextual information to align the vocabulary found in the source code with that found in other software artifacts. We were inspired in the choice of context levels by prior works and by our findings. Normalization consists of two tasks: splitting and expansion of source code identifiers. We also investigate the effect of source code vocabulary normalization approaches on software maintenance tasks. Results of our evaluation show that our contextual-aware techniques are accurate and efficient in terms of computation time than state of the art alternatives. In addition, our findings reveal that feature location techniques can benefit from vocabulary normalization when no dynamic information is available. © 2013 IEEE.

| MD        | ER  | MC  | VL  | DG  |
| --------- | --- | --- | --- | --- |
| unsure/no |     | no  |     | no  |

* *MD* - "we propose source code vocabulary normalization approaches"
* *MC* - too specific, and probably subjective. Probably related to design patterns, *à la Gang of Four*.
* *DG* - This may be useful for metadata representation, but not SQ

---

## 44 - Enhancing defect tracking systems to facilitate software quality improvement

### Li J., Stalhane T., Conradi R., Kristiansen J.M.W.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-84863297555&doi=10.1109%2fMS.2011.24&partnerID=40&md5=e741c2dc3eecffec2fa5e97a54b547a6

For projects that rely on empirical process control and deliver frequently working versions of software, developers and project managers regularly need to examine the status of their software quality. This study illustrates that simple goal-oriented changes or extensions to the existing data of projects' respective defect tracking systems could provide valuable and prompt information to improve their software quality assessment and assurance. © 2012 IEEE.

| MD  ---| ER  | MC  | VL  | DG  |
| ------ | --- | --- | --- | --- |
| unsure |     | no  |     | no  |

---

## 56 - Concurrency design patterns, software quality attributes and their tactics

### Zheng J., Harper K.E.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-77954570582&doi=10.1145%2f1808954.1808964&partnerID=40&md5=46cfdf02f74de1d4d8809d601743a0e5

With the prevalent application of multi-core CPUs, software practitioners are facing the challenge of developing high quality multi-threaded programs. Applying concurrency design patterns is one of the best practices in multi-core software engineering. We comprehensively surveyed 28 concurrency design patterns, and provided a problem-oriented guide that navigates software developers towards the "right" pattern(s) with minimal search/reading effort. The guide also illustrates the relationship between concurrency design patterns and the quality attributes they address. Additionally, further investigation was conducted on how these concurrency design patterns implement quality attributes tactics. We present a mapping between surveyed concurrency design patterns and the tactics for two important quality attributes: performance and modifiability. The results of these studies provide an insight into concurrency design patterns for software developers who are seeking appropriate or improved solutions to multi-threaded software development issues. © 2010 ACM.

| MD     | ER  | MC  | VL  | DG  |
| ------ | --- | --- | --- | --- |
| unsure |     |     |     | no  |

* *MD* - probably check the quality attributes in the paper.
* *MC* - perhaps too specific, but it can be useful for the Landscaping, to find specific quality criteria for research SW running, for example, in large clusters. I'm thinking in the research SW of the SKA radiotelescope, or the data analysis infraestructure at CERN, for example.

---

## 57 - When process data quality affects the number of bugs: Correlations in software engineering datasets

### Bachmann A., Bernstein A.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-77953774300&doi=10.1109%2fMSR.2010.5463286&partnerID=40&md5=8998845e532edbb8dc25941ad5697894

Software engineering process information extracted from version control systems and bug tracking databases are widely used in empirical software engineering. In prior work, we showed that these data are plagued by quality deficiencies, which vary in its characteristics across projects. In addition, we showed that those deficiencies in the form of bias do impact the results of studies in empirical software engineering. While these findings affect software engineering researchers the impact on practitioners has not yet been substantiated. In this paper we, therefore, explore (i) if the process data quality and characteristics have an influence on the bug fixing process and (ii) if the process quality as measured by the process data has an influence on the product (i.e., software) quality. Specifically, we analyze six Open Source as well as two Closed Source projects and show that process data quality and characteristics have an impact on the bug fixing process: the high rate of empty commit messages in Eclipse, for example, correlates with the bug report quality. We also show that the product quality - measured by number of bugs reported - is affected by process data quality measures. These findings have the potential to prompt practitioners to increase the quality of their software process and its associated data quality. © 2010 IEEE.

| MD     | ER  | MC  | VL  | DG  |
| ------ | --- | --- | --- | --- |
| unsure |     | no  |     | no  |

* *MC* - I'm not very confident on all the papers discussing "correlations", since I don't expect them to provide any actual discussion on quality criteria itself.

---

## 59 - A fuzzy regression and optimization approach for setting target levels in software quality function deployment

### Sener Z., Karsak E.E.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-77953480593&doi=10.1007%2fs11219-010-9095-6&partnerID=40&md5=90014463ba282d5a711f45572e77d3c0

With the rapid development of the software industry, improving the quality of software development has gained increasing importance. Software manufacturers have recently applied quality improvement techniques to software development to respond to the needs for software quality. Software quality function deployment (SQFD), as a technique for improving the quality of the software development process to create products responsive to customer expectations, is used to maximize customer satisfaction. This paper presents a fuzzy regression and optimization approach to determine target levels in SQFD. The inherent fuzziness of relationships in SQFD modeling justifies the use of fuzzy regression. Fuzzy regression is used to identify the functional relationships between customer requirements and technical attributes, and among technical attributes. Then, a mathematical programming model is developed to determine target levels of technical attributes using the functional relationships obtained by fuzzy regression. A search engine quality improvement problem is presented to illustrate the application of the proposed approach. © 2010 Springer Science+Business Media, LLC.

| MD        | ER  | MC  | VL  | DG  |
| --------- | --- | --- | --- | --- |
| unsure/no |     | no  |     | no  |

* *MC* - too domain-specific.

---

## 60 - Software quality, non-functional software requirements and IT-business alignment

### Haigh M.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-77953478255&doi=10.1007%2fs11219-010-9098-3&partnerID=40&md5=c282adcc1b14f37b160afdc5cae38f7d

'High quality' might seem an obvious requirement for any piece of software, but do the different stakeholder groups involved in its production and use conceptualize this requirement in the same way? Many existing models refine the broad concept of quality into a number of well-defined and measurable attributes related to the software product itself and the development process which produced it. But despite growing awareness of the importance of achieving cultural alignment between holders of different business and IT groups, little attempt has been made to empirically examine the requirements for software quality held by different groups involved in the development process. We conducted a survey of more than 300 current and recently graduated students of one of the leading Executive MBA programs in the United States, asking them to rate the importance of each of 13 widely-cited attributes related to software quality. The results showed business role-related differences in some specific areas and agreement in many others. The results suggest that a strong shared culture may be able to bridge the gulf created between holders of IT and business stakeholder roles. © 2010 Springer Science+Business Media, LLC.

| MD     | ER  | MC  | VL  | DG  |
| ------ | --- | --- | --- | --- |
| unsure |     | no  |     | no  |

* *MD* - check reference to 13 widely-cited attributes related to software quality
* *MC* - probably not very objective and also based on correlations.
* *DG* - +1 to that suggestion

---

## 66 - Does distributed development affect software quality? An empirical case study of windows vista

### Bird C., Nagappan N., Devanbu P., Gall H., Murphy B.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-77949887177&doi=10.1109%2fICSE.2009.5070550&partnerID=40&md5=b2268150b63c60366c76b7fa3a7dd644

It is widely believed that distributed software development is riskier and more challenging than collocated development. Prior literature on distributed development in software engineering and other fields discuss various challenges, including cultural barriers, expertise transfer dif-ficulties, and communication and coordination overhead. We evaluate this conventional belief by examining the overall development of Windows Vista and comparing the postrelease failures of components that were developed in a distributed fashion with those that were developed by collocated teams. We found a negligible difference in failures. This difference becomes even less significant when controlling for the number of developers working on a binary. We also examine component characteristics such as code churn, complexity, dependency information, and test code coverage and find very little difference between distributed and collocated components to investigate if less complex components are more distributed. Further, we examine the software process and phenomena that occurred during the Vista development cycle and present ways in which the development process utilized may be insensitive to geography by mitigating the difficulties introduced in prior work in this area. © 2009 IEEE.

| MD  | ER      | MC  | VL  | DG  |
| --- | ------- | --- | --- | --- |
| no  |  unsure | no  |     | no  |

* *ER* - this should talk about software metrics, maybe it introduces some software characteristics in relation to the software metrics selected.
* *MD* - seems just distributed vs collocated teams comparison
* *MC* - more focused on organizational aspects than quality.

---

## 73 - Rational quality requirements for medical software

### Paech B., Wetter T.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-57349160287&doi=10.1145%2f1368088.1368176&partnerID=40&md5=ee7159688c9ff44dfeee64f309aa9661

In this paper we discuss the challenges of software quality for medical software and present some ideas for improving medical software quality requirements through software engineering methods. We apply the quality requirements engineering method MOQARE to elicit specific quality requirements for an imaginary drug advisory system and report our lessons learned. Copyright 2008 ACM.

| MD        | ER  | MC     | VL  | DG  |
| --------- | --- | ------ | --- | --- |
| unsure/no |     | unsure |     | no  |

* *MC* - I'd do a quick read to see if they provide any actual criteria specific to medical imaging SW.

---

## 80 - Software quality requirements: How to balance competing priorities

### Blaine J.D., Cleland-Huang J.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-40949089293&doi=10.1109%2fMS.2008.46&partnerID=40&md5=92cff91e274c9915234437f2b7b9e83e

The elicitation, analysis, and specification of quality requirements involve careful balancing of a broad spectrum of competing priorities. Developers must therefore focus on identifying qualities and designing solutions that optimize the product's value to its stakeholders. © 2008 IEEE.

| MD        | ER  | MC  | VL  | DG  |
| --------- | --- | --- | --- | --- |
| unsure/no |     | no  |  no | no  |

---

## 81 - Integrating fuzzy theory and hierarchy concepts to evaluate software quality

### Chang C.-W., Wu C.-R., Lin H.-L.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-42149193088&doi=10.1007%2fs11219-007-9035-2&partnerID=40&md5=c0726b7b8745845e0160bf4ff0966f32

This study proposes a software quality evaluation model and its computing algorithm. Existing software quality evaluation models examine multiple characteristics and are characterized by factorial fuzziness. The relevant criteria of this model are derived from the international norm ISO. The main objective of this paper is to propose a novel Analytic Hierarchy Process (AHP) approach for addressing uncertainty and imprecision in service evaluation during pre-negotiation stages, where comparative judgments of decision makers are represented as fuzzy triangular numbers. A new fuzzy prioritization method, which derives crisp priorities from consistent and inconsistent fuzzy comparison matrices, is proposed. The Fuzzy Analytic Hierarchy Process (FAHP)-based decision-making method can provide decision makers or buyers with a valuable guideline for evaluating software quality. Importantly, the proposed model can aids users and developers in assessing software quality, making it highly applicable for academic and commercial purposes. © 2007 Springer Science+Business Media, LLC.

| MD        | ER  | MC  | VL  | DG  |
| --------- | --- | --- | --- | --- |
| unsure/no |     | no  | no  | no  |

* *MC* - too domain-specific.

---

## 86 - Using fault slippage measurement for monitoring software process quality during development

### Damm L.-O., Lundberg L.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-84885655995&doi=10.1145%2f1137702.1137707&partnerID=40&md5=a72e3ef2602755e39c97e34a92a563e9

In a competitive environment where time-to-market is crucial for success, software development companies initiate process improvement programs that can shorten the development time. They especially seek improvements in the verification activities since rework commonly constitutes a significant part of the development cost. However, the success of process improvement initiatives is dependent on early and observable results since a lack of feedback on the effect of improvements is a common cause of failure. This paper investigates how to monitor the verification process as input to decisions such as improvement actions. The suggested approach was applied on three industrial software products at Ericsson and the results determined that the approach can be used for quantitative monitoring of process quality and as decision support to do rapid improvement actions. © 2006 ACM.

| MD        | ER  | MC  | VL  | DG  |
| --------- | --- | --- | --- | --- |
| unsure/no |     | no  | no  | no  |

* *MC* - probably based on the performance of the monitor SW, rather than criteria on SW itself.

---

## 102 - Requirements engineering and process modelling in software quality management - Towards a generic process metamodel

### Berki E., Georgiadou E., Holcombe M.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-3142676780&doi=10.1023%2fB%3aSQJO.0000034711.87241.f0&partnerID=40&md5=57a51d22bc656cff90603f0d24ae4251

This paper examines the concept of Quality in Software Engineering, its different contexts and its different meanings to various people. It begins with a commentary on quality issues for systems development and various stakeholders' involvement. It revisits aspects and concepts of systems development methods and highlights the relevance of quality issues to the choice of a process model. A summarised review of some families of methods is presented, where their application domain, lifecycle coverage, strengths and weaknesses are considered. Under the new development era the requirements of software development change; the role of methods and stakeholders change, too. The paper refers to the latest developments in the area of software engineering and emphasises the shift from traditional conceptual modelling to requirements engineering and process metamodelling principles. We provide support for an emerging discipline in the form of a software process metamodel to cover new issues for software quality and process improvement. The widening of the horizons of software engineering both as a 'communication tool' and as a 'scientific discipline' (and not as a 'craft') is needed in order to support both communicative and scientific quality systems properties. In general, we can consider such a discipline as a thinking tool for understanding the generic process and as the origin of combining intuition and quality engineering to transform requirements to adequate human-centred information systems. We conclude with a schematic representation of a Generic Process Metamodel (GPM) indicating facets contributed by Software Engineering, Computer Science, Information Systems, Mathematics, Linguistics, Sociology and Anthropology. Ongoing research and development issues have provided evidence for influence from even more diverse disciplines.

| MD     | ER     | MC  | VL  | DG  |
| ------ | ------ | --- | --- | --- |
| unsure | unsure | no  |     | no  |

* *ER* - useful for introducing the problem

---

## 104 - Analogy-Based Practical Classification Rules for Software Quality Estimation

### Khoshgoftaar T.M., Seliya N.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-0141924286&doi=10.1023%2fA%3a1025316301168&partnerID=40&md5=c55c23db4d307f95d3a30705f91b2729

Software metrics-based quality estimation models can be effective tools for identifying which modules are likely to be fault-prone or not fault-prone. The use of such models prior to system deployment can considerably reduce the likelihood of faults discovered during operations, hence improving system reliability. A software quality classification model is calibrated using metrics from a past release or similar project, and is then applied to modules currently under development. Subsequently, a timely prediction of which modules are likely to have faults can be obtained. However, software quality classification models used in practice may not provide a useful balance between the two misclassification rates, especially when there are very few faulty modules in the system being modeled. This paper presents, in the context of case-based reasoning, two practical classification rules that allow appropriate emphasis on each type of misclassification as per the project requirements. The suggested techniques are especially useful for high-assurance systems where faulty modules are rare. The proposed generalized classification methods emphasize on the costs of misclassifications, and the unbalanced distribution of the faulty program modules. We illustrate the proposed techniques with a case study that consists of software measurements and fault data collected over multiple releases of a large-scale legacy telecommunication system. In addition to investigating the two classification methods, a brief relative comparison of the techniques is also presented. It is indicated that the level of classification accuracy and model-robustness observed for the case study would be beneficial in achieving high software reliability of its subsequent system releases. Similar observations are made from our empirical studies with other case studies.

| MD     | ER     | MC  | VL  | DG  |
| ------ | ------ | --- | --- | --- |
| unsure | unsure | no  |     | no  |

* *ER* - useful for software metrics
* *MC* - I think that authors might have found interesting correlations between SW quality and system failures, but I don't think this article is useful to define quality itself.

---

## 110 - Software component quality assessment in practice: Successes and practical impediments

### Gorton I., Liu A.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-0036038348&partnerID=40&md5=f02adf14ad9f74556313950b1f9bdd34

This paper describes the authors' experiences of initiating and sustaining a project at CSIRO aimed at accelerating the successful adoption of COTS middleware technologies in large business and scientific information systems. The projects aims are described, along with example outcomes and an assessment of what is needed for wide-scale software component quality assessments to succeed.

| MD     | ER  | MC     | VL  | DG  |
| ------ | --- | ------ | --- | --- |
| unsure |     | unsure |     | no  |

* *MC* - we might have a look at the criteria, but I'm not confident their concept to 'quality' is the same as us.

---

## 111 - Examining the Effect of the Transformational Leader on Software Quality

### Parzinger M.J., Nath R., Lemons M.A.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-0042547833&doi=10.1023%2fA%3a1013763119819&partnerID=40&md5=7d31b7d93f78b6c4d5642bf4db7bae43

Developing and maintaining quality software is paramount in the information-intensive society. A myriad of concepts, tools and techniques exist that can be employed to improve the quality of software and at the same time increase developmental efficiencies. Approaches used by many software development units include: Capability Maturity Model (CMM), Total Quality Management (TQM), and ISO 9000-3. Implementation of these approaches without appropriate management oversight does not guarantee success. This study examines the role of the manager vis-à-vis "leadership style" with software quality. Data collected using a questionnaire administered to members of the American Society for Quality (ASQ) - Software Division, suggest that the Transformational leadership style of the manager has a significant positive relationship with the quality of the software developed.

| MD        | ER  | MC  | VL  | DG  |
| --------- | --- | --- | --- | --- |
| unsure/no |     | no  |     | no  |

* *MC* - it seems more related to management than to quality criteria.

---

## 113 - Quality through Managed Improvement and Measurement (QMIM): Towards a Phased Development and Implementation of a Quality Management System for a Software Company

### Balla K., Bemelmans T., Kusters R., Trienekens J.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-0010645865&doi=10.1023%2fA%3a1013301503616&partnerID=40&md5=cfe9889727ca12badee4d71ce1c02868

The paper describes results of a longitudinal study of developments in the area of software product and process quality improvement within a Hungarian software company, IQSOFT Ltd. This company has been active in this area since 1993, trying to build, introduce and maintain an efficiently working quality management system which, e.g., fulfils the ISO 9001 requirements, allows steady software process improvement and, at the same time, conforms to company's own needs. Over the last eight years five phases could be distinguished. Each phase is described shortly, following the same structure, namely: basic starting points, key problem areas, literature consulted, activities and design executed, reflections on what happened and why. The lessons resulting from the analysis of this case have been formulated in terms of guidelines. We feel that these are applicable to any low maturity software development organisation embarking on a product or process quality improvement endeavour. These guidelines are developed around a framework containing the basic issues of software production (project management, technical processes and products). The guidelines advocate a careful step-by-step development of definitions, quality characteristics, and metrics related to these objects while at the same time developing and introducing the associated process.

| MD        | ER     | MC  | VL  | DG  |
| --------- | ------ | --- | --- | --- |
| unsure/no | unsure | no  |     | no  |

* *ER* - useful for software development process
* *MC* - management of organizations, not that much about quality itself.

---

## 115 - A quality software process for rapid application development

### Coleman G., Verbruggen R.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-0542397516&doi=10.1023%2fA%3a1008856624790&partnerID=40&md5=f6924e80eaf9d9671e402727a974b77f

Software organizations can significantly improve the quality of their output if they have a defined and documented software process, together with the appropriate techniques and tools to measure its effectiveness. Without a defined process it is impossible to measure success or focus on how development capability can be enhanced. To date, a number of software process improvement frameworks have been developed and implemented. However, most of these models have been targeted at large-scale producers. Furthermore, they have applied to companies who use traditional development techniques. Smaller companies and those operating in development areas where speed of delivery is paramount have not, as yet, had process improvement paradigms available for adoption. This study examined the software process in a small company and emerged with the recommendation of the use of the Dynamic Systems Development Method (DSDM) and the Personal Software Process (PSP) for achieving software process improvement.

| MD        | ER  | MC  | VL  | DG  |
| --------- | --- | --- | --- | --- |
| unsure/no |     | no  |     | no  |

* *MC* - this one proposed a methodology to ensure quality. It's worth to have a look to the proposed criteria. Perhaps also useful for "SW in prod".

---

## 125 - The impact of software evolution and reuse on software quality

### Khoshgoftaar T.M., Allen E.B., Kalaichelvan K.S., Goel N.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-0029726553&doi=10.1007%2fBF00125810&partnerID=40&md5=22f6cf0451a62716aa68a29a14e0ca89

This paper presents a case study of a software project in the maintenance phase. The case study was based on a sample of modules, representing about 1.3 million lines of code, from a very large telecommunications system. Software quality models were developed to predict the number of faults expected from the coding through operations phases. Since modules from the prior release were often reused to develop a new release, one model incorporated reuse data as additional independent variables. We compare this model's performance to a similar model without reuse data. Software quality models often have product metrics as the only input data for predicting quality. There is an implicit assumption that all the modules have had a similar development history, so that product attributes are the primary drivers of different quality levels. Reuse of software as components and software evolution do not fit this assumption very well, and consequently, traditional models for such environments may not have adequate accuracy. Focusing on the software maintenance phase, this study demonstrated that reuse data can significantly improve the predictive accuracy of software quality models. © 1996 Kluwer Academic Publishers.

| MD  | ER  | MC  | VL     | DG  |
| --- | --- | --- | ------ | --- |
|     |     | no  | unsure | no  |

* *MC* - it seems to be focused on the benefits of "reuse of data", not on quality of SW itself.

---

## 132 - Measurement as an alternative to bureaucracy for the achievement of software quality

### Neil M.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-1542478267&doi=10.1007%2fBF00213631&partnerID=40&md5=d7492a6bd3774989e38bb87ab5119d87

In this paper we discuss the two dominant modes of thought on the problem of software quality: the bureaucratic approach and the technical approach. The aim of the paper is to pursue the issues of how these approaches affect people, in our case software developers, and how we can assess the effectiveness of each approach in actually achieving quality software. An outline of the main aspects of the organizational approach - process modelling and software standards - is given. In order to address the effects of each of these modes of thought on people we take a psychological perspective. The implications for software engineering, in terms of formalism and mechanization, are discussed. The paper argues that overzealous structure, control and automation can negatively affect the creative process of developing software. A perspective on each of the components of the technical approach in terms of their effectiveness in achieving quality objectives is provided. From recent work we find that process modelling and many software standards do not provide an adequate assessment of the benefits derived from their application. The paper argues that measurement goes some way to addressing these problems. Measurement should form the core of the software development process, especially with respect to product quality assessment. The main conclusion is that by focusing on measurable objectives and results we can best achieve quality software products and highlight the processes which are likely to create them in a repeatable and manageable fashion. Additionally, by adopting measurement in practice we should expect to increase the freedom and creativity of software developers. © 1994 Chapman & Hall.

| MD  | ER  | MC  | VL     | DG  |
| --- | --- | --- | ------ | --- |
|     |     | no  | unsure | no  |

* *MC* - probably about organization, not quality itself.

---

## 138 - Reliable software and communication: software quality, reliability, and safety

### Dalal S.R., Horgan J.R., Kettenring J.R.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-0027208332&doi=10.1109%2fICSE.1993.346023&partnerID=40&md5=7ffb40c895d81738e0e5f41e5e1e5fed

The software created by industrial, educational, and research organizations is increasingly large and complex. It also occupies a central role in the reliability and safety of many essential services. We examine the software development process and suggest opportunities for improving the process by using a combination of statistical and other process control techniques. Data, analysis of data, and tools for collecting data are crucial to our approach. Though our views are based upon experiences with large telecommunications systems, they are likely to be useful to many other developers of large software systems.

| MD  | ER  | MC  | VL     | DG  |
| --- | --- | --- | ------ | --- |
|     |     | no  | unsure | no  |

* *MC* - this doesn't seem related to quality itself.

---

## 142 - Application of software reliability modeling to product quality and test process

### Ehrlich Willa K., Stampfel John P., Wu Jar R.

### https://www.scopus.com/inward/record.uri?eid=2-s2.0-0025135323&partnerID=40&md5=b4dbdc121b20e110987e3f1af36ed7e5

Software reliability modeling of data collected during the testing of a large-scale industrial system (System T) was used to measure software quality from the customer perspective. Specifically, software quality was measured in terms of the system operation. The testing phase analyzed, stability test, was an operational profile-driven test in that a controlled load was imposed on the system reflective of the system's busy-hour usage pattern. The usage profile was determined from requirements specifying both the frequency of invocation of each command and the alarm arrival rate for the largest expected user site. For this controlled test environment, a Poisson-type reliability growth model, the exponential nonhomogeneous Poisson process model, exhibited a good fit to the observed failure data. Furthermore, the model demonstrated predictive power for future failure rates. It is concluded that the use of an operational profile to drive system test is an effective test strategy and that the operational profile must be taken into account when predicting field reliability from reliability measured during test.

| MD        | ER  | MC  | VL  | DG  |
| --------- | --- | --- | --- | --- |
| unsure/no |     | no  | no  | no  |

* *MD* - measure SW reliability in production/operation
* *MC* - it seems to be considering "product quality" as non-faulty and "from the customer perspective". It might provide some hints for us, but I don't think it's worth it.
