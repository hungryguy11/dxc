using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using Assessment_EF.Models;

namespace Assessment_EF.Controllers
{
    public class HomeController : Controller
    {
        public ActionResult Index()
        {
            DBfirstdemoEntities2 context = new DBfirstdemoEntities2();
            DisplayList model = new DisplayList();
            model.desList = context.Designations.ToList();
            model.empList = context.People.ToList();
            return View(model);
        }

        public ActionResult About()
        {
            ViewBag.Message = "Your application description page.";

            return View();
        }

        public ActionResult Contact()
        {
            ViewBag.Message = "Your contact page.";

            return View();
        }
    }
}