This project is to monitor the azure resource created in subscription and manage the best practices for Azure resources
Set-up your environment to work wiht Azure  https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-node-azure-pack
Set you development environment with latest python libraries 
   python -m pip install --upgrade pip   # to update your python installer to latest version
   pip install azure-mgmt-resource     #to install latest Azure Management libraries 
   pip install azure-identity   # to install Azure Identity libraries 
As a best practice create requirements.txt file to list all the required libraries in your proejct 










Out Put :
PS C:\development\python\AzureAdministrationwihtPython> pip install azure-mgmt-resource    
Collecting azure-mgmt-resource
  Downloading azure_mgmt_resource-20.0.0-py2.py3-none-any.whl (2.3 MB)
     |████████████████████████████████| 2.3 MB 3.3 MB/s
Collecting azure-common~=1.1
  Downloading azure_common-1.1.27-py2.py3-none-any.whl (12 kB)
Collecting msrest>=0.6.21
  Downloading msrest-0.6.21-py2.py3-none-any.whl (85 kB)
     |████████████████████████████████| 85 kB 923 kB/s
Collecting azure-mgmt-core<2.0.0,>=1.2.0
  Downloading azure_mgmt_core-1.3.0-py2.py3-none-any.whl (25 kB)
Collecting azure-core<2.0.0,>=1.15.0
  Downloading azure_core-1.18.0-py2.py3-none-any.whl (166 kB)
     |████████████████████████████████| 166 kB 6.4 MB/s
Collecting requests>=2.18.4
  Downloading requests-2.26.0-py2.py3-none-any.whl (62 kB)
     |████████████████████████████████| 62 kB 354 kB/s
Collecting six>=1.11.0
  Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)
Collecting certifi>=2017.4.17
  Downloading certifi-2021.5.30-py2.py3-none-any.whl (145 kB)
     |████████████████████████████████| 145 kB 6.4 MB/s
Collecting isodate>=0.6.0
  Downloading isodate-0.6.0-py2.py3-none-any.whl (45 kB)
     |████████████████████████████████| 45 kB 1.6 MB/s
Collecting requests-oauthlib>=0.5.0
  Downloading requests_oauthlib-1.3.0-py2.py3-none-any.whl (23 kB)
Collecting urllib3<1.27,>=1.21.1
  Downloading urllib3-1.26.6-py2.py3-none-any.whl (138 kB)
     |████████████████████████████████| 138 kB 6.8 MB/s
Collecting idna<4,>=2.5
  Downloading idna-3.2-py3-none-any.whl (59 kB)
     |████████████████████████████████| 59 kB ...
Collecting charset-normalizer~=2.0.0
  Downloading charset_normalizer-2.0.6-py3-none-any.whl (37 kB)
Collecting oauthlib>=3.0.0
  Downloading oauthlib-3.1.1-py2.py3-none-any.whl (146 kB)
     |████████████████████████████████| 146 kB 6.4 MB/s
Installing collected packages: urllib3, idna, charset-normalizer, certifi, six, requests, oauthlib, requests-oauthlib, isodate, azure-core, msrest, azure-mgmt-core, azure-common, azure-mgmt-resource
Successfully installed azure-common-1.1.27 azure-core-1.18.0 azure-mgmt-core-1.3.0 azure-mgmt-resource-20.0.0 certifi-2021.5.30 charset-normalizer-2.0.6 idna-3.2 isodate-0.6.0 msrest-0.6.21 oauthlib-3.1.1 requests-2.26.0 requests-oauthlib-1.3.0 six-1.16.0 urllib3-1.26.6


PS C:\development\python\AzureAdministrationwihtPython> pip install azure-identity     
Collecting azure-identity
  Downloading azure_identity-1.6.1-py2.py3-none-any.whl (109 kB)
     |████████████████████████████████| 109 kB 939 kB/s
Requirement already satisfied: six>=1.12.0 in c:\users\vigodava\appdata\local\programs\python\python38-32\lib\site-packages (from azure-identity) (1.16.0)
Requirement already satisfied: azure-core<2.0.0,>=1.0.0 in c:\users\vigodava\appdata\local\programs\python\python38-32\lib\site-packages (from azure-identity) (1.18.0)
Collecting cryptography>=2.1.4
  Downloading cryptography-3.4.8-cp36-abi3-win32.whl (1.4 MB)
     |████████████████████████████████| 1.4 MB 3.3 MB/s
Collecting msal-extensions~=0.3.0
  Downloading msal_extensions-0.3.0-py2.py3-none-any.whl (16 kB)
Collecting msal<2.0.0,>=1.7.0
  Downloading msal-1.14.0-py2.py3-none-any.whl (75 kB)
     |████████████████████████████████| 75 kB 1.3 MB/s
Requirement already satisfied: requests>=2.18.4 in c:\users\vigodava\appdata\local\programs\python\python38-32\lib\site-packages (from azure-core<2.0.0,>=1.0.0->azure-identity) (2.26.0)
Collecting cffi>=1.12
  Downloading cffi-1.14.6-cp38-cp38-win32.whl (167 kB)
     |████████████████████████████████| 167 kB 6.4 MB/s
Collecting pycparser
  Downloading pycparser-2.20-py2.py3-none-any.whl (112 kB)
     |████████████████████████████████| 112 kB 6.4 MB/s
Collecting PyJWT[crypto]<3,>=1.0.0
  Downloading PyJWT-2.1.0-py3-none-any.whl (16 kB)
Collecting portalocker~=1.6
  Downloading portalocker-1.7.1-py2.py3-none-any.whl (10 kB)
Collecting pywin32!=226
  Downloading pywin32-301-cp38-cp38-win32.whl (8.5 MB)
     |████████████████████████████████| 8.5 MB 6.4 MB/s
Requirement already satisfied: certifi>=2017.4.17 in c:\users\vigodava\appdata\local\programs\python\python38-32\lib\site-packages (from requests>=2.18.4->azure-core<2.0.0,>=1.0.0->azure-identity) (2021.5.30)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\users\vigodava\appdata\local\programs\python\python38-32\lib\site-packages (from requests>=2.18.4->azure-core<2.0.0,>=1.0.0->azure-identity) (1.26.6)
Requirement already satisfied: charset-normalizer~=2.0.0 in c:\users\vigodava\appdata\local\programs\python\python38-32\lib\site-packages (from requests>=2.18.4->azure-core<2.0.0,>=1.0.0->azure-identity) (2.0.6)
Requirement already satisfied: idna<4,>=2.5 in c:\users\vigodava\appdata\local\programs\python\python38-32\lib\site-packages (from requests>=2.18.4->azure-core<2.0.0,>=1.0.0->azure-identity) (3.2)
Installing collected packages: pycparser, cffi, PyJWT, cryptography, pywin32, portalocker, msal, msal-extensions, azure-identity
Successfully installed PyJWT-2.1.0 azure-identity-1.6.1 cffi-1.14.6 cryptography-3.4.8 msal-1.14.0 msal-extensions-0.3.0 portalocker-1.7.1 pycparser-2.20 pywin32-301
PS C:\development\python\AzureAdministrationwihtPython> 