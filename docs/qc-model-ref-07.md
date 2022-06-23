# QM Reference 07: (paper ID = 93)

Reviewer: MC (Miguel Colom)

Early estimation of software quality using in-process testing metrics: A controlled case study, Nagappan N., Williams L., Vouk M., Osborne J.
<https://www.scopus.com/inward/record.uri?eid=2-s2.0-77955433687&doi=10.1145%2f1083292.1083304&partnerID=40&md5=c3b21a87b407b65539153ab3017b0eda>

| Codename | Name  | Definition | Aut(omate)/Man(ual) | Category | Comment |
| :------: | :---: | :--------: | :-----------------: | :------: | :-----: |
|SM1|Number of assertions SLOC|number of lines of source code containing assertions|Aut|Reliability||
|SM2|Number of test cases SLOC*|number of lines of source code containing test cases that check that the program is behaving as expected|Aut|Reliability|it refers to tests intented to be automated, as for example unit test cases|
|SM3|number of assertions / number of test cases|ratio number of assertions / number of test cases|Aut|Reliability||
|SM4|control measure to counter the confounding effect of class size on the prediction efficiency|(TLOC+/SLOC*) / (number of test classes / number of source classes)|Aut|Reliability||
|SM5|cyclomatic complexity test/source ratio|ratio between the sum of cyclomatic complexities of all tests and the whole source code|Aut|Complexity|the "cyclomatic complexity" is the number of linearly independent paths in a program. Graph theory applied to software analysis. The paper doesn't provide details on how this metric is calculated exactly.|
|SM6|coupling between objects (CBO) ratio|ratio between the CBO in the tests and the whole source code|Aut|Complexity||
|SM7|depth of inheritance tree (DIT) ratio|ratio between the DIT of the tests and the DIT of the whole source code|Aut|Complexity||
|SM8|weighted methods per class (WMC) ratio|ratio between the WMC of the tests with respect of the WMC of the whole source code|Aut|Complexity|it can be automated if the size of the "weighted" object is a parameter|
|SM9|SLOC* ratio|SLOC* of the whole project with respect to the minimum SLOC* of its components|Aut|Complexity||

