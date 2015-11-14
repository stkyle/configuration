#
#
"""

"""
import ConfigParser

sample_config = """
[DEFAULT]
# Comment A

[SectionOne]
Status: Single
Name: Derek
Value: Yes

# Comment B
# Comment C
Age: 30
Single: True

[SectionTwo]
FavoriteColor=Green
[SectionThree]
FamilyName: Johnson

[Others]
Route: 66
"""


config = ConfigParser.ConfigParser()
config.readfp(sample_config)
print(config.sections())
