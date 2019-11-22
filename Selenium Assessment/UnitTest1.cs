using System;
using System.Threading;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Firefox;
using OpenQA.Selenium.Interactions;

namespace Unit_TestDemo
{
    [TestClass]
    public class UnitTest1
    {
        [TestMethod]
        public void TestMethod1()
        {
            string[] elements_id = { "emergencyFund", "investments", "retirement", "food", "clothing", "shelter", "household", "transportation", "health", "studentLoans", "personal", "misc","tuition","homeowners","car","taxes","vacation","other","monthlyPay","monthlyOther","annualGifts","annualTaxReturn" };
            string[] link_texts = { "Calculators & Resources", "Calculators", "Budget Calculator" };
            string emergencyFund, investments, retirement, food, clothing, shelter, household, transportation, health, studentLoans, personal, misc, tuition, homeowners, car, taxes, vacation, other, monthlyPay, monthlyOther, annualGifts, annualTaxReturn;
            string url = "http://www.youcandealwithit.com/";
            //IWebDriver driver = new ChromeDriver("C:\\Selenium Jars");
            IWebDriver driver = new FirefoxDriver("C:\\Selenium Jars");
            driver.Url = url;
            driver.Manage().Window.Maximize();
            driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(30);
            IWebElement borrower = driver.FindElement(By.XPath("//a[text()='Borrowers']"));
            Actions action = new Actions(driver);
            action.MoveToElement(borrower).Build().Perform();
            
            driver.FindElement(By.LinkText(link_texts[0])).Click();
            Thread.Sleep(3000);
            if (driver.Title.Equals(link_texts[0] + " - YouCanDealWithIt"))
                Console.WriteLine($"link-text : {link_texts[0]} passed");
            else
                Console.WriteLine($"link-text : {link_texts[0]} failed");
            driver.FindElement(By.LinkText(link_texts[1])).Click();
            Thread.Sleep(3000);

            if (driver.Title.Equals(link_texts[1] + " - YouCanDealWithIt"))
                Console.WriteLine($"link-text : {link_texts[1]} passed");
            else
                Console.WriteLine($"link-text : {link_texts[1]} failed");
            driver.FindElement(By.LinkText(link_texts[2])).Click();
            Thread.Sleep(3000);

            if (driver.Title.Equals(link_texts[2] + " - YouCanDealWithIt"))
                Console.WriteLine($"link-text : {link_texts[2]} passed");
            else
                Console.WriteLine($"link-text : {link_texts[2]} failed");
           
            driver.FindElement(By.Id(elements_id[0])).SendKeys(emergencyFund = "3000");
            driver.FindElement(By.Id(elements_id[1])).SendKeys(investments="4000");
            driver.FindElement(By.Id(elements_id[2])).SendKeys(retirement="5000");
            driver.FindElement(By.Id(elements_id[3])).SendKeys(food="4000");
            driver.FindElement(By.Id(elements_id[4])).SendKeys(clothing="3000");
            driver.FindElement(By.Id(elements_id[5])).SendKeys(shelter="2000");
            driver.FindElement(By.Id(elements_id[6])).SendKeys(household="3000");
            driver.FindElement(By.Id(elements_id[7])).SendKeys(transportation="2000");
            driver.FindElement(By.Id(elements_id[8])).SendKeys(health="5000");
            driver.FindElement(By.Id(elements_id[9])).SendKeys(studentLoans="4000");
            driver.FindElement(By.Id(elements_id[10])).SendKeys(personal="4500");
            driver.FindElement(By.Id(elements_id[11])).SendKeys(misc="3000");
            Thread.Sleep(3000);
            driver.FindElement(By.Id(elements_id[12])).SendKeys(tuition = "3400");
            driver.FindElement(By.Id(elements_id[13])).SendKeys(homeowners = "4500");
            driver.FindElement(By.Id(elements_id[14])).SendKeys(car = "5000");
            driver.FindElement(By.Id(elements_id[15])).SendKeys(taxes = "4500");
            driver.FindElement(By.Id(elements_id[16])).SendKeys(vacation = "3400");
            driver.FindElement(By.Id(elements_id[17])).SendKeys(other = "7600");
            driver.FindElement(By.Id(elements_id[18])).SendKeys(monthlyPay = "80000");
            driver.FindElement(By.Id(elements_id[19])).SendKeys(monthlyOther = "4500");
            driver.FindElement(By.Id(elements_id[20])).SendKeys(annualGifts = "34000");
            driver.FindElement(By.Id(elements_id[21])).SendKeys(annualTaxReturn = "20000");

            Thread.Sleep(3000);

            double budget = double.Parse(driver.FindElement(By.Id("underOverBudget")).GetAttribute("value"));
            double monthlypay = double.Parse(driver.FindElement(By.Id("monthlyPay")).GetAttribute("value"));
            double monthlyexpense = double.Parse(driver.FindElement(By.Id("totalMonthlyExpenses")).GetAttribute("value"));

            Console.WriteLine($"Monthly Pay : {monthlypay}");
            Console.WriteLine($"Monthly Expenses :{monthlyexpense}" );
            

            if(monthlyexpense>= monthlypay)
            {
                Console.WriteLine("You are Warren Buffet");
                Console.WriteLine($"Over Budget : {budget}");
            }
            else
            {
                Console.WriteLine("You are VM");
                Console.WriteLine($"Under Budget : {budget}");
            }

            driver.Close();





        }
    }
}
