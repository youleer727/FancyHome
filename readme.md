# Properties Management
## (COMS4111, Project 1, Part 3)


### PostgreSQL account:
```bash
psql -Uxl2672 -h 104.196.18.7 -d w4111
```
### Group UNI
```bash
Jun Hu (jh3846)& Xiyan Liu (xl2672)
```
### URL
[http://104.155.207.69:8111/]

### Implementation
We have implemented all the features in Part1, and made the web application interact with all the data in Part 2. In below, ```Web Map``` shows all the main features of our website.

### Web Application Mapping
* HOME
    * BUYER
        * HEADER LINKS
            * ```HOME```
            * ```BUYER```
            * ```AGENT```
        * FUNCTIONS
            * Multiple Choices Search For Properties By
                1. minimum bedroom
                2. minimum bathroom
                3. minimum size
                4. maximum size
                5. minimum list price
                6. maximum list price
                7. water front
                8. tax abatement
                9. sale state
                    * ```SEARCH RETURN RESULTS AND All FUNCTIONS AVAILABLE```
            * Multiple Choices Search For Agents By
                1. minimum registered properties number
                2. minimum on sale properties number
                3. minimum sold properties number
                4. minimum average list price
                5. maximum average list price
                6. minimum average sold price
                7. maximum average sold price
                    * ```SEARCH RETURN RESULTS AND All FUNCTIONS AVAILABLE```
        * INFORMATION
            * Featured Properties (Show Some Recommended Properties)
                1. property id
                2. zip code
                3. address
                4. bedroom
                5. bathroom
                6. size
                7. built date
                8. district
                9. water front
                10. bus
                11. subway
                12. list date
                13. list price
                14. evaluated price
                15. tax abatement
                16. maintenance fee
                17. agent id
                    * ```Click``` Functions (used universally, not only for featured properties)
                        * schools will show the clicked property
                            1. primary schools
                            2. middle schools
                            3. high schools
                        * contact agent will show the chosen property's agent
                            1. common agent information (16 items)
                            2. properties on sale by this agent
                            3. properties sold by this agent
            * Gold Agents (Show Some Best Agents)
                1. agent id
                2. full name
                3. cell phone
                4. email
                5. number of all properties
                6. number of on sale properties
                7. number of sold properties
                8. max price ever listed
                9. min price ever listed
                10. average listed price
                11. max price ever sold
                12. min price ever sold
                13. average sold price
                14. max price evaluated
                15. min price evaluated
                16. average evaluated price
                    * ```Click``` Functions (used universally, not only for featured properties)
                        * contact agent will show the chosen property's agent
                            1. common agent information (16 items)
                            2. properties on sale by this agent
                            3. properties sold by this agent
    * AGENT
        * LOGIN
            * Invalid ---> Alert and Retrun ```LOGIN```
            * Valid ---> ```DASHBOARD```
        * DASHBOARD
            * HEADER LINKS
                * ```HOME```
                * ```BUYER```
                * ```AGENT```
            * FUNCTIONS
                * List New Properties
                    1. property id (automatically generate)
                    2. zip code
                    3. address
                    4. bedroom
                    5. bathroom
                    6. size
                    7. built date
                    9. district
                    10. water front
                    11. list price
                    12. evaluated price
                    13. tax abatement
                    14. maintenance fee
                    15. owner ssn
                    16. owner first name
                    17. owner last name
                    18. list date (today automatically recorded)
                        * ```CLICK EXECUTE INSERT AND RETURN UPDATED DASHBOARD```
            * INFORMATION
                * The Agent Own
                    1. agent id
                    2. full name
                    3. cell phone
                    4. email
                    5. number of all properties
                    6. number of on sale properties
                    7. number of sold properties
                    8. max price ever listed
                    9. min price ever listed
                    10. average listed price
                    11. max price ever sold
                    12. min price ever sold
                    13. average sold price
                    14. max price evaluated
                    15. min price evaluated
                    16. average evaluated price
                        * Click Functions (used universally, not only for featured properties)
                            * contact agent will show the chosen property's agent
                                1. common agent information (16 items)
                                2. properties on sale by this agent
                                3. properties sold by this agent
                * Properties On Sale By The Agent
                    1. property id
                    2. zip code
                    3. address
                    4. bedroom
                    5. bathroom
                    6. size
                    7. built date
                    8. district
                    9. water front
                    10. bus
                    11. subway
                    12. list date
                    13. list price
                    14. evaluated price
                    15. tax abatement
                    16. maintenance fee
                    17. agent id
                    18. owner ssn
                    19. owner full name
                        * ```Click``` Functions (used universally, not only for featured properties)
                            * schools will show the clicked property
                                1. primary schools
                                2. middle schools
                                3. high schools
                * Properties Sold By The Agent
                    1. property id
                    2. zip code
                    3. address
                    4. bedroom
                    5. bathroom
                    6. size
                    7. built date
                    8. district
                    9. water front
                    10. bus
                    11. subway
                    12. list date
                    13. list price
                    14. evaluated price
                    15. tax abatement
                    16. maintenance fee
                    17. agent id
                    18. sold price
                    19. owner ssn
                    20. owner full name
                        * ```Click``` Functions (used universally, not only for featured properties)
                            * schools will show the clicked property
                                1. primary schools
                                2. middle schools
                                3. high schools
### Agents Login Info
| ﻿agnt_email                           | password |
|--------------------------------------|----------|
| Jessamine.Wells@bestrealestate.com   | agnt1    |
| Marshall.Flores@realestate4u.com     | agnt2    |
| Eric.Stewart@hotmail.com             | agnt3    |
| Celeste.Chapman@gmail.com            | agnt4    |
| Joy.Potts@wonderproperty.com         | agnt5    |
| Tucker.Brady@21centry.com            | agnt6    |
| Shelly.Collins@vipagent.com          | agnt7    |
| Danielle.Green@bestrealestate.com    | agnt8    |
| Lewis.Valdez@realestate4u.com        | agnt9    |
| Hoyt.Pittman@hotmail.com             | agnt10   |
| Xandra.Haynes@gmail.com              | agnt11   |
| Cheyenne.Smith@wonderproperty.com    | agnt12   |
| Kamal.Wells@21centry.com             | agnt13   |
| Keith.Sanford@vipagent.com           | agnt14   |
| Montana.Faulkner@bestrealestate.com  | agnt15   |
| Dustin.Ramos@realestate4u.com        | agnt16   |
| Bernard.Saunders@hotmail.com         | agnt17   |
| Zane.Mayo@gmail.com                  | agnt18   |
| Coby.Frank@wonderproperty.com        | agnt19   |
| Marshall.Mcmillan@21centry.com       | agnt20   |
| Raya.Mullins@vipagent.com            | agnt21   |
| Xaviera.Riley@bestrealestate.com     | agnt22   |
| Leonard.Rhodes@realestate4u.com      | agnt23   |
| Bianca.Floyd@hotmail.com             | agnt24   |
| Tyler.Crawford@gmail.com             | agnt25   |
| Porter.Carrillo@wonderproperty.com   | agnt26   |
| Jenette.Chapman@21centry.com         | agnt27   |
| Armand.Mccarthy@vipagent.com         | agnt28   |
| Cameron.Cardenas@bestrealestate.com  | agnt29   |
| Marcia.Blevins@realestate4u.com      | agnt30   |
| Kane.Kent@hotmail.com                | agnt31   |
| Norman.Park@gmail.com                | agnt32   |
| Destiny.Herrera@wonderproperty.com   | agnt33   |
| Madonna.Lambert@21centry.com         | agnt34   |
| Aubrey.Holmes@vipagent.com           | agnt35   |
| Abigail.Holman@bestrealestate.com    | agnt36   |
| Camilla.Nichols@realestate4u.com     | agnt37   |
| Madeline.Stanton@hotmail.com         | agnt38   |
| Sylvia.Fitzgerald@gmail.com          | agnt39   |
| Alexander.Randall@wonderproperty.com | agnt40   |
| Simon.French@21centry.com            | agnt41   |
| Rinah.Shepherd@vipagent.com          | agnt42   |
| Slade.Arnold@bestrealestate.com      | agnt43   |
| Brynne.Cain@realestate4u.com         | agnt44   |
| Callie.Chambers@hotmail.com          | agnt45   |
| Hedda.Sherman@gmail.com              | agnt46   |
| Germane.Kirk@wonderproperty.com      | agnt47   |

