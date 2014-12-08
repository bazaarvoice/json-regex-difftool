Contributing
=================

Bug reports, feature requests, and code contribution are all greatly appreciated. 


##Bug Reports

When reporting bugs please provide the full command with arguments, input files used, and program output of the failing command.

##Feature Request

Before submitting a new feature request, please search through the list of [existing issues](https://github.com/bazaarvoice/json-regex-difftool/issues) to ensure that the request is not a duplicate. 

##Code Contribution

Before working on a new feature, bug fix or documentation patch, please browse the [existing issues](https://github.com/bazaarvoice/json-regex-difftool/issues) to see whether it has been previously discussed. If the change is large in scale, it's always better to discus before starting work.

####Checking out the code

```bash
# first fork the repository to your account (click the fork button)
# Clone the repo locally
git clone https://github.com/<YOU>/json-regex-difftool
# Change to json-regex-difftool root
cd json-regex-difftool
# Checkout a new branch
git checkout -b my_feature_or_bug_fix
```

####Making Changes

Please make sure your changes conform to the [PEP8 Style Guide](https://www.python.org/dev/peps/pep-0008/).

####Tests

Before opening pull requests please make sure the [test suite](https://github.com/bazaarvoice/json-regex-difftool/tree/master/test) passes in all of the supported python environments. **Tests should be included for any pull request for a new feature or a bug fix.**

json-regex-difftool uses [nose](https://nose.readthedocs.org/en/latest/) for running tests.
