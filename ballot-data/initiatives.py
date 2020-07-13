import requests
from bs4 import BeautifulSoup
import boto3


#calling url
page = requests.get("https://info.kingcounty.gov/kcelections/Vote/contests/ballotmeasures.aspx?lang=en-US&cid=99713&groupname=SpecialPurposeDistrict")
soup = BeautifulSoup(page.text, 'html.parser')

#pulling out needed info
ballot = soup.find(class_ = "well").get_text()
exp = soup.find_all(class_ = "panel-title")[0].get_text() + soup.find(id = "explanatorystatement").get_text()
statement_for = soup.find_all(class_ = "panel-title")[1].get_text() + soup.find(id = "statementfor").get_text()
statement_against = soup.find_all(class_ = "panel-title")[2].get_text() + soup.find(id = "statementagainst").get_text()
pass_req = soup.find_all(class_ = "panel-title")[4].get_text() + soup.find(id = "validationrules").get_text()

paragraph_text = ballot + exp + statement_for + statement_against + pass_req
print(paragraph_text)
