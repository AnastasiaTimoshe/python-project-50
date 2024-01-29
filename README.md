### Hexlet tests and linter status:
[![Actions Status](https://github.com/AnastasiaTimoshe/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/AnastasiaTimoshe/python-project-50/actions)

[![CI check](https://github.com/AnastasiaTimoshe/python-project-50/actions/workflows/project-check.yml/badge.svg)](https://github.com/AnastasiaTimoshe/python-project-50/actions/workflows/project-check.yml)

[![Maintainability](https://api.codeclimate.com/v1/badges/e67a45e3e5acbe0fdfdc/maintainability)](https://codeclimate.com/github/AnastasiaTimoshe/python-project-50/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/e67a45e3e5acbe0fdfdc/test_coverage)](https://codeclimate.com/github/AnastasiaTimoshe/python-project-50/test_coverage)


## Description


Difference generator is a program that determines the difference between two data structures.
A program is able to work with the formats: ```json```, ```yaml```


## Installation


Clone the repository and use this commands:

```
make install
make build
make package-install
```


## Optional arguments

1. **-h, --help**  `gendiff -h` - launch help
2. **-f, --format** `gendiff -f` - set format of output. **Available formats:**
* `-f stylish` - default format
* `-f plain`
* `-f json`


### Comparison of flat files (JSON)

`gendiff filepath1.json filepath2.json`

[![asciicast](https://asciinema.org/a/SL8AvymVBCW2sKYNmU7fhJalt.svg)](https://asciinema.org/a/SL8AvymVBCW2sKYNmU7fhJalt)



### Comparison of flat files (YAML, YML)

`gendiff filepath1.yaml filepath2.yaml`

[![asciicast](https://asciinema.org/a/diyc9R5ryNxCvqkVT3oIJ69dd.svg)](https://asciinema.org/a/diyc9R5ryNxCvqkVT3oIJ69dd)


### Comparison of two files with a recursive structure (JSON, YAML, YML)

`gendiff filepath1.json filepath2.json`

[![asciicast](https://asciinema.org/a/i4SW9pHEOxXA8UUNATou1oNBO.svg)](https://asciinema.org/a/i4SW9pHEOxXA8UUNATou1oNBO)


### Work example formatter PLAIN

`gendiff filepath1.json filepath2.json -f plain`

[![asciicast](https://asciinema.org/a/UDnP6qRpQejZouGOElEUcc94a.svg)](https://asciinema.org/a/UDnP6qRpQejZouGOElEUcc94a)


### Work example formatter JSON

`gendiff filepath1.json filepath2.json -f json`

[![asciicast](https://asciinema.org/a/PCwMoMi8YRWBiKaiQZtvFWMGi.svg)](https://asciinema.org/a/PCwMoMi8YRWBiKaiQZtvFWMGi)