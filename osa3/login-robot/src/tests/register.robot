*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  juuso  juuso12345
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  toimivasalasana!
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  x  toimivasalasana123
    Output Should Contain  Username is too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  juusopetteri99  toimivasalasana123
    Output Should Contain  Username can only contain letters from a-z

Register With Valid Username And Too Short Password
    Input Credentials  juusopetteri  eitoimi
    Output Should Contain  Password has to be at least 8 letters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  juusopetteri  eitoimitaas
    Output Should Contain  Password cannot contain only letters

*** Keywords ***
Create User And Input New Command
    
    Create User  kalle  kalle12345
    Input New Command