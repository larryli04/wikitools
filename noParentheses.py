import copy

def noParentheses(string):
    if ("(" in string):
        pass
    else:
        return string
    pcounter = 1

    string = "" + str(string)

    start = string.index("(")
    end = 0
    for i in range(start+1, len(string)):
        if string[i] == "(":
            pcounter += 1
        elif string[i] == ")":
            pcounter -= 1
        
        if pcounter == 0:
            end = i
            break



    return string[0:start] + string[end+1:]

def noBracket(string):

    # print(string.count("{"))
    # print(string.count("}"))

    string = string.replace("\n", "")
    pcounter = 1

    string = "" + str(string)

    start = string.index("{")

    end = 0
    for i in range(start+1, len(string)):
        if string[i] == "{":
            pcounter += 1
        elif string[i] == "}":
            pcounter -= 1
        
        if pcounter == 0:
            end = i

            return string[:start] + string[end+1:], False
        # print(pcounter)

    return string, True
    # exit() # something bad happened

def isFile(string):

    if("[[File:" in string or "[[Image:" in string):
        return True
    else:
        return False
def noFile(string):
    if("[[File:" in string):
        start=string.index("[[File:")
        pass
    elif("[[Image:" in string):
        start=string.index("[[Image:")
        pass
    else:
        return string

    pcounter = 1
    end = 0
    for i in range(start+1, len(string)):
        if string[i] == "[":
            pcounter += 1
        elif string[i] == "]":
            pcounter -= 1
        
        if pcounter == 0:
            end = i
            return string[0:start] + string[end+1:], False
    #     print(pcounter)
    # print(end)
    # take out [[File:...]], image, etc

    return string, True

print(noFile("asdf[[File:[[asdfa]]]]asdfa"))

def noApos(string): # not used anymore
    try:
        index = string.index(r"'''")
    except:
        # print("No bold text found, probably a redirect")
        return string, True # pass something that says its a redirect
    # print(string)
    return string[index:], False

def flink(string):



    string = "" + str(string)

    start = string.index("[[")

    end = 0
    for i in range(start+1, len(string)):
        
        if string[i] == "]":
            end = i

            break
        # print(pcounter)
    s = string[start+2:end]

    if("|" in s):
        bar_index = s.index("|")
        return s[bar_index+1:end-1]
    return string[start+2:end]

def link(string):
    return string[2:-2]

def redirect(string):
    return flink(string[9:])

def clean(string):
    s = string
    
    if(string[0] == "#"):
        return None, True
    if(not "[" in string):
        return None, True
    s = noParentheses(s)
    f = False
    while((len(s) != 0 and "{" in s and f==False)):
        if(s.index("[")<s.index("{")):
            break
        s,f = noBracket(s)
        
    while(isFile(s) and f==False):
        # print("please no")
        s,f = noFile(s)
    
        # print(s[:50])
        
        # print(s[:2000])
    


    # get rid of newlines
    # s = s.replace("\n", "")


    # start at bold text
    # print(noApos(string)[:50])
    return s, False

t = '''{{Short description|none}}
{{US taxation}}
{{PoliticsUS}}
The [[United States|United States of America]] has separate [[Federal government of the United States|federal]], [[U.S. state|state]], and [[Local government in the United States|local government]]s with [[tax]]es imposed at each of these levels. Taxes are levied on income, payroll, property, sales, [[Capital gains tax in the United States|capital gains]], dividends, imports, estates and gifts, as well as various fees. In 2020, taxes collected by federal, state, and local governments amounted to 25.5% of [[GDP]], below the [[OECD]] average of 33.5% of GDP. The United States had the seventh-lowest tax revenue-to-GDP ratio among OECD countries in 2020, with a higher ratio than [[Mexico]], [[Colombia]], [[Chile]], [[Republic of Ireland|Ireland]], [[Costa Rica]], and [[Turkey]].&lt;ref&gt;Organization for Economic Co-operation and Development (OECD), 2021. ''Revenue Statistics 2021: The Initial Impact of COVID-19 on OECD Tax Revenues'', OECD Publishing, Paris, [[doi:10.1787/6e87f932-en|https://doi.org/10.1787/6e87f932-en.]] Tax-to-GDP figures for 2020 are preliminary.&lt;/ref&gt;

Taxes fall much more heavily on labor income than on capital income. Divergent taxes and subsidies for different forms of income and spending can also constitute a form of indirect taxation of some activities over others. For example, individual spending on higher education can be said to be &quot;taxed&quot; at a high rate, compared to other forms of personal expenditure which are formally recognized as investments.

Taxes are imposed on [[Income tax|net income]] of individuals and corporations by the federal, most state, and some local governments. Citizens and residents are taxed on worldwide income and allowed a credit for foreign taxes. Income subject to tax is determined under tax accounting rules, not financial accounting principles, and includes almost all income from whatever source. Most business expenses reduce taxable income, though limits apply to a few expenses. Individuals are permitted to reduce taxable income by personal allowances and certain non-business expenses, including [[Home mortgage interest deduction|home mortgage interest]], [[State and local tax deduction|state and local taxes]], [[Charitable contribution deductions in the United States|charitable contributions]], and medical and certain other expenses incurred above certain percentages of income. State rules for determining taxable income often differ from federal rules. Federal marginal [[tax rate]]s vary from 10% to 37% of taxable income.&lt;ref&gt;{{Cite web|last=Internal Revenue Service|date=October 26, 2020|title=IRS Provides Tax Inflation Adjustments for Tax Year 2021 (IR-2020-245)|url=https://www.irs.gov/newsroom/irs-provides-tax-inflation-adjustments-for-tax-year-2021|url-status=live|access-date=December 18, 2021}}&lt;/ref&gt; State and local tax rates vary widely by jurisdiction, from 0% to 13.30% of income,&lt;ref&gt;{{cite web|url=http://vig.cdn.sos.ca.gov/2012/general/pdf/30-title-summ-analysis.pdf |title=TEMPORARY TAXES TO FUND EDUCATION. GUARANTEED LOCAL PUBLIC SAFETY FUNDING. INITIATIVE CONSTITUTIONAL AMENDMENT |publisher=Vig.cdn.sos.ca.gov/ |date=2013-04-05 |access-date=2013-10-13}}&lt;/ref&gt; and many are graduated. State taxes are generally treated as a deductible expense for federal tax computation, although the [[Tax Cuts and Jobs Act of 2017|2017 tax law]] imposed a $10,000 limit on the state and local tax (&quot;SALT&quot;) deduction, which raised the effective tax rate on medium and high earners in high tax states. Prior to the SALT deduction limit, the average deduction exceeded $10,000 in most of the Midwest, and exceeded $11,000 in most of the Northeastern United States, as well as California and Oregon.&lt;ref name=&quot;:0&quot;&gt;{{Cite web|url=https://www.forbes.com/sites/chuckdevore/2018/07/26/new-york-and-other-high-tax-states-sue-over-salt-deduction-cap-while-jobs-follow-lower-taxes/|title=New York And Other High-Tax States Sue Over SALT Deduction Cap While Jobs Follow Lower Taxes|last=DeVore|first=Chuck|website=Forbes|language=en|access-date=2019-01-08}}&lt;/ref&gt; The states impacted the most by the limit were the [[tri-state area]] (NY, NJ, and CT) and California; the average SALT deduction in those states was greater than $17,000 in 2014.&lt;ref name=&quot;:0&quot; /&gt;

The United States is one of two countries in the world that [[International taxation#Citizenship|taxes its non-resident citizens]] on worldwide income, in the same manner and rates as residents; the other is [[Eritrea]]. The U.S. Supreme Court upheld the constitutionality of imposition of such a tax in the case of ''Cook v. Tait''.&lt;ref&gt;265 U.S. 47 (1924).&lt;/ref&gt;

[[Payroll tax]]es are imposed by the federal and all state governments. These include Social Security and Medicare taxes imposed on both employers and employees, at a combined rate of 15.3% (13.3% for 2011 and 2012). Social Security tax applies only to the first $132,900 of wages in 2019.&lt;ref name=&quot;:1&quot;&gt;{{Cite web|url=https://www.adp.com/resources/articles-and-insights/articles/e/eow-social-security-wage-base-for-2019-announced.aspx|title=Social Security Wage Base for 2019 Announced|date=2015-06-30|website=www.adp.com|language=en|access-date=2019-11-13}}&lt;/ref&gt; There is an additional Medicare tax of 0.9% on wages above $200,000. Employers must withhold income taxes on wages. An unemployment tax and certain other levies apply to employers. Payroll taxes have dramatically increased as a share of federal revenue since the 1950s, while corporate income taxes have fallen as a share of revenue. (Corporate profits have not fallen as a share of GDP).

[[Property tax]]es are imposed by most local governments and many special purpose authorities based on the fair market value of property. School and other authorities are often separately governed, and impose separate taxes. Property tax is generally imposed only on realty, though some jurisdictions tax some forms of business property. Property tax rules and rates vary widely with annual median rates ranging from 0.2% to 1.9% of a property's value depending on the state.&lt;ref&gt;{{cite web|url=http://www.tax-rates.org/taxtables/property-tax-by-state|title=Property Taxes By State|publisher=Tax-Rates.org|date=2009|access-date=2015-02-01}}&lt;/ref&gt;

[[Sales tax]]es are imposed by most states and some localities on the price at retail sale of many goods and some services. Sales tax rates vary widely among jurisdictions, from 0% to 16%, and may vary within a jurisdiction based on the particular goods or services taxed. Sales tax is collected by the seller at the time of sale, or remitted as use tax by buyers of taxable items who did not pay sales tax.

The United States imposes tariffs or [[customs]] duties on the import of many types of goods from many jurisdictions. These tariffs or duties must be paid before the goods can be legally imported. Rates of duty vary from 0% to more than 20%, based on the particular goods and country of origin.

[[Inheritance tax|Estate]] and [[gift tax]]es are imposed by the federal and some state governments on the transfer of property inheritance, by will, or by lifetime donation. Similar to federal income taxes, federal estate and gift taxes are imposed on worldwide property of citizens and residents and allow a credit for foreign taxes.
[[File:Taxes revenue by source chart history.png|frameless|upright=1.8|right|Taxes revenue by source chart history]]
[[File:Government Revenue and spending GDP.png|400px|right]]
[[File:Federal taxes by type.pdf|thumb|upright=1.8|Federal taxes by type]]
'''
# print("here", clean(t))

f = '''"The [[United States|United States of America]] has separate [[Federal government of the United States|federal]], [[U.S. state|state]], and [[Local government in the United States|local government]]s with [[tax]]es imposed at each of these levels. Taxes are levied on income, payroll, property, sales, [[Capital gains tax in the United States|capital gains]], dividends, imports, estates and gifts, as well as various fees. In 2020, taxes collected by federal, state, and local governments amounted to 25.5% of [[GDP]], below the [[OECD]] average of 33.5% of GDP. The United States had the seventh-lowest tax revenue-to-GDP ratio among OECD countries in 2020, with a higher ratio than [[Mexico]], [[Colombia]], [[Chile]], [[Republic of Ireland|Ireland]], [[Costa Rica]], and [[Turkey]].&lt;ref&gt;Organization for Economic Co-operation and Development , 2021. ''Revenue Statistics 2021: The Initial Impact of COVID-19 on OECD Tax Revenues'', OECD Publishing, Paris, [[doi:10.1787/6e87f932-en|https://doi.org/10.1787/6e87f932-en.]] Tax-to-GDP figures for 2020 are preliminary.&lt;/ref&gt;Taxes fall much more heavily on labor income than on capital income. Divergent taxes and subsidies for different forms of income and spending can also constitute a form of indirect taxation of some activities over others. For example, individual spending on higher education can be said to be &quot;taxed&quot; at a high rate, compared to other forms of personal expenditure which are formally recognized as investments.Taxes are imposed on [[Income tax|net income]] of individuals and corporations by the federal, most state, and some local governments. Citizens and residents are taxed on worldwide income and allowed a credit for foreign taxes. Income subject to tax is determined under tax accounting rules, not financial accounting principles, and includes almost all income from whatever source. Most business expenses reduce taxable income, though limits apply to a few expenses. Individuals are permitted to reduce taxable income by personal allowances and certain non-business expenses, including [[Home mortgage interest deduction|home mortgage interest]], [[State and local tax deduction|state and local taxes]], [[Charitable contribution deductions in the United States|charitable contributions]], and medical and certain other expenses incurred above certain percentages of income. State rules for determining taxable income often differ from federal rules. Federal marginal [[tax rate]]s vary from 10% to 37% of taxable income.&lt;ref&gt;{{Cite web|last=Internal Revenue Service|date=October 26, 2020|title=IRS Provides Tax Inflation Adjustments for Tax Year 2021 (IR-2020-245)|url=https://www.irs.gov/newsroom/irs-provides-tax-inflation-adjustments-for-tax-year-2021|url-status=live|access-date=December 18, 2021}}&lt;/ref&gt; State and local tax rates vary widely by jurisdiction, from 0% to 13.30% of income,&lt;ref&gt;{{cite web|url=http://vig.cdn.sos.ca.gov/2012/general/pdf/30-title-summ-analysis.pdf |title=TEMPORARY TAXES TO FUND EDUCATION. GUARANTEED LOCAL PUBLIC SAFETY FUNDING. INITIATIVE CONSTITUTIONAL AMENDMENT |publisher=Vig.cdn.sos.ca.gov/ |date=2013-04-05 |access-date=2013-10-13}}&lt;/ref&gt; and many are graduated. State taxes are generally treated as a deductible expense for federal tax computation, although the [[Tax Cuts and Jobs Act of 2017|2017 tax law]] imposed a $10,000 limit on the state and local tax (&quot;SALT&quot;) deduction, which raised the effective tax rate on medium and high earners in high tax states. Prior to the SALT deduction limit, the average deduction exceeded $10,000 in most of the Midwest, and exceeded $11,000 in most of the Northeastern United States, as well as California and Oregon.&lt;ref name=&quot;:0&quot;&gt;{{Cite web|url=https://www.forbes.com/sites/chuckdevore/2018/07/26/new-york-and-other-high-tax-states-sue-over-salt-deduction-cap-while-jobs-follow-lower-taxes/|title=New York And Other High-Tax States Sue Over SALT Deduction Cap While Jobs Follow Lower Taxes|last=DeVore|first=Chuck|website=Forbes|language=en|access-date=2019-01-08}}&lt;/ref&gt; The states impacted the most by the limit were the [[tri-state area]] (NY, NJ, and CT) and California; the average SALT deduction in those states was greater than $17,000 in 2014.&lt;ref name=&quot;:0&quot; /&gt;The United States is one of two countries in the world that [[International taxation#Citizenship|taxes its non-resident citizens]] on worldwide income, in the same manner and rates as residents; the other is [[Eritrea]]. The U.S. Supreme Court upheld the constitutionality of imposition of such a tax in the case of ''Cook v. Tait''.&lt;ref&gt;265 U.S. 47 (1924).&lt;/ref&gt;[[Payroll tax]]es are imposed by the federal and all state governments. These include Social Security and Medicare taxes imposed on both employers and employees, at a combined rate of 15.3% (13.3% for 2011 and 2012). Social Security tax applies only to the first $132,900 of wages in 2019.&lt;ref name=&quot;:1&quot;&gt;{{Cite web|url=https://www.adp.com/resources/articles-and-insights/articles/e/eow-social-security-wage-base-for-2019-announced.aspx|title=Social Security Wage Base for 2019 Announced|date=2015-06-30|website=www.adp.com|language=en|access-date=2019-11-13}}&lt;/ref&gt; There is an additional Medicare tax of 0.9% on wages above $200,000. Employers must withhold income taxes on wages. An unemployment tax and certain other levies apply to employers. Payroll taxes have dramatically increased as a share of federal revenue since the 1950s, while corporate income taxes have fallen as a share of revenue. (Corporate profits have not fallen as a share of GDP).[[Property tax]]es are imposed by most local governments and many special purpose authorities based on the fair market value of property. School and other authorities are often separately governed, and impose separate taxes. Property tax is generally imposed only on realty, though some jurisdictions tax some forms of business property. Property tax rules and rates vary widely with annual median rates ranging from 0.2% to 1.9% of a property's value depending on the state.&lt;ref&gt;{{cite web|url=http://www.tax-rates.org/taxtables/property-tax-by-state|title=Property Taxes By State|publisher=Tax-Rates.org|date=2009|access-date=2015-02-01}}&lt;/ref&gt;[[Sales tax]]es are imposed by most states and some localities on the price at retail sale of many goods and some services. Sales tax rates vary widely among jurisdictions, from 0% to 16%, and may vary within a jurisdiction based on the particular goods or services taxed. Sales tax is collected by the seller at the time of sale, or remitted as use tax by buyers of taxable items who did not pay sales tax.The United States imposes tariffs or [[customs]] duties on the import of many types of goods from many jurisdictions. These tariffs or duties must be paid before the goods can be legally imported. Rates of duty vary from 0% to more than 20%, based on the particular goods and country of origin.[[Inheritance tax|Estate]] and [[gift tax]]es are imposed by the federal and some state governments on the transfer of property inheritance, by will, or by lifetime donation. Similar to federal income taxes, federal estate and gift taxes are imposed on worldwide property of citizens and residents and allow a credit for foreign taxes.[[File:Taxes revenue by source chart history.png|frameless|upright=1.8|right|Taxes revenue by source chart history]][[File:Government Revenue and spending GDP.png|400px|right]][[File:Federal taxes by type.pdf|thumb|upright=1.8|Federal taxes by type]]"'''
# print("there", flink(f))
# print()
# print(noBracket(t))
# print("-----------------------------------------------------------------")
# print(noBracket(noBracket(t)))
# print("-----------------------------------------------------------------")
# print(noBracket(noBracket(noBracket(t))))
# print("-----------------------------------------------------------------")
# print(noBracket(noBracket(noBracket(noBracket(t)))))




# print(clean(r"{{short description|Political philosophy and movement}}{{other uses}}{{redirect2|Anarchist|Anarchists|other uses|Anarchist (disambiguation)}}{{distinguish|Anarchy}}{{pp-semi-indef}}{{good article}}{{use British English|date=August 2021}}{{use dmy dates|date=August 2021}}{{anarchism sidebar}}{{basic forms of government}}"))