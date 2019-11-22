using System;
using System.Text;
using System.Collections.Generic;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using System.Threading;

namespace Unit_TestDemo
{
 
    [TestClass]
    public class UnitTest2
    {
        public static void Main(string[] args)
        {
            UnitTest2 test = new UnitTest2();
            test.TestMethod1();
        }



        [TestMethod]
        public void TestMethod1()
        {
            string textbox_name = "q";
            string button_name = "btnK";
            string result_id = "resultStats";
            IWebDriver driver = new ChromeDriver("C:\\Selenium Jars");
            driver.Url = "https://www.google.com/";
            Thread.Sleep(3000);
            string search = "DXC Technologies";
            driver.FindElement(By.Name(textbox_name)).SendKeys(search);
            Thread.Sleep(2000);
            driver.FindElement(By.Name(button_name)).Click();
            string title = driver.Title;
            string result = driver.FindElement(By.Id(result_id)).Text;
            Console.WriteLine(driver.Title);
            Console.WriteLine(result);
            Console.WriteLine(search);
            search += " - Google Search";
            if (title.Equals(search))
            {
                Console.WriteLine("Pass");
            }
            else
            {
                Console.WriteLine("Fail");
            }
            driver.Close();
           
            
         
        }
    }
}
