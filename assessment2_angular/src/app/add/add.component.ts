import { Component, OnInit } from '@angular/core';
import { Department } from '../department';
import { DepartmentService } from '../department.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-add',
  templateUrl: './add.component.html',
  styleUrls: ['./add.component.scss']
})
export class AddComponent implements OnInit {

  department = new Department();

  constructor(private svc :DepartmentService, private route :Router) { }

  ngOnInit() {
  }

  addList(){

    this.svc.save(this.department);
    console.log(this.department);
    this.route.navigate(['list']);
    
  }

}
