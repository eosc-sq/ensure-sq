# QM Reference 16: (paper ID = 154)

Reviewer:  MD (Mario David)

Reference: (ID = 154) - Software Release Practice HOWTO, Eric Steven Raymond,
<https://tldp.org/HOWTO/Software-Release-Practice-HOWTO/>

| Codename | Name  | Definition | Aut(omate)/Man(ual) | Category | Comment |
| :------: | :---: | :--------: | :-----------------: | :------: | :-----: |
| 2   | Good patching practice | open-source software by writing patches | Man | | |
| 3   | Good project- and archive- naming practice | important for project and archive-file names to fit regular patterns that computer programs can parse and understand. | Aut | | Yes: include |
| 3.1 | Use GNU-style names with a stem and major.minor.patch numbering | all-lower-case alphanumeric stem prefix, followed by a dash, followed by a version number, extension, and other suffixes. | Aut | | Yes: include (c.f. semantic versioning) |
| 3.2 | But respect local conventions where appropriate | Some projects and communities have well-defined conventions for names and version numbers that aren't necessarily compatible with the above advice. | Man | | As exception to the above |
| 3.3 | Try hard to choose a name prefix that is unique and easy to type | The stem prefix should be easy to read, type, and remember | Man | | Yes: include |
| 4   | Good licensing and copyright practice: the theory | The license you choose defines the social contract you wish to set up among your co-developers and users. | Aut | | Yes: include |
| 5 | Good licensing and copyright practice: the practice | | | | same as 4 |
| 6 | Good development practice | Most of these are concerned with ensuring portability across all POSIX and POSIX-like systems | Aut | | |
| 6.1 | Choose the most portable language you can | Choose a development language which minimizes the differences of the underlying environments in which it will run. | Man | | No: developer choose whatever program language as he sees fit |
| 6.2 | Don't rely on proprietary code | Don't rely on proprietary languages, libraries, or other code | | Aut | Yes: include |
| 6.3 | Build systems | A significant advantage of open source distributions is they allow each source package to adapt at compile-time to the environment it finds. | Aut | | Yes: include (Cont Delivery) |
| 6.4 | Test your code before release | A good test suite allows the team to buy inexpensive hardware for testing and then easily run regression tests before releases.  | Aut | | Yes: include (Cont Integration) |
| 6.5 | Sanity-check your code before release | If you're writing C/C++ using GCC, test-compile with -Wall and clean up all warning messages before each release. Compile your code with every compiler you can find — different compilers often find different problems. Specifically, compile your software on true 64-bit machine. Underlying data types can change on 64-bit machines, and you will often find new problems there. Find a UNIX vendor's system and run the lint utility over your software. Run tools that for memory leaks and other run-time errors; Electric Fence and Valgrind are two good ones available in open source.For Python projects, the PyChecker program can be a useful check. It's not out of beta yet, but nevertheless often catches nontrivial errors. If you're writing Perl, check your code with perl -c (and maybe -T, if applicable). Use perl -w and 'use strict' religiously. | Aut | | Yes: include (Cont Integration) |
| 6.6 | Sanity-check your documentation and READMEs before release | Spell-check your documentation, README files and error messages in your software. | Man | Documentation | Yes: include |
| 6.7 | Recommended C/C++ portability practices | If you are writing C, feel free to use the full ANSI features. | Man | | Yes: include (although specific for C/C++ code) |
| 7 | Good distribution-making practice | | | | |
| 7.1 | Make sure tarballs always unpack into a single new directory | The single most annoying mistake newbie developers make is to build tarballs that unpack the files and directories in the distribution into the current directory, potentially stepping on files already located there. Never do this! | Aut | | Yes: include |
| 7.2 | Have a README | Have a file called README or READ.ME that is a roadmap of your source distribution | Aut | Documentation | Yes: include |
| 7.3 | Respect and follow standard file naming practices | standard top-level file names: README INSTALL AUTHORS NEWS HISTORY COPYING LICENSE MANIFEST FAQ TAGS| Aut | Documentation | Yes: include |
| 7.4 | Design for Upgradability | Your software will change over time as you put out new releases. Some of these changes will not be backward-compatible. Accordingly, you should give serious thought to designing your installation layouts so that multiple installed versions of your code can coexist on the same system. This is especially important for libraries — you can't count on all your client programs to upgrade in lockstep with your API changes | Man | | Yes: include |
| 7.5 | Provide checksums | Provide checksums with your binaries (tarballs, RPMs, etc.). | Aut | | Yes: include |
| 8 | Good documentation practice | The most important good documentation practice is to actually write some | | | |
| 8.1 | Documentation formats | Here are the documentation markup formats now in widespread use among open-source developers. man pages, HTML Texinfo DocBook asciidoc | Aut | Documentation | Yes: include |
| 8.2 | Good practice recommendations | Maintain your document masters in either XML-DocBook or asciidoc. Ship the XML or asciidoc masters. Generate XHTML from your masters | Aut | Documentation | Yes maybe, there are newer formats now more common |
| 9 | Good communication practice | our software and documentation won't do the world much good if nobody but you knows it exists. | Man | | Yes: include - public visibility and availability |
| 10 | Good project-management practice | | Man | | Yes partly this is very generic |
