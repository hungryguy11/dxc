import { Component, OnInit } from '@angular/core';
import { Department } from '../department';
import { DepartmentService } from '../department.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.scss']
})
export class ListComponent implements OnInit {

  department : Department;
  updatediv = false;
  indexposition :number;
  deptList : Department[];

  constructor(private svc :DepartmentService , private route :Router) { }

  ngOnInit() {

    this.deptList = this.svc.deptList;
  }

  edit (index:number)
  {
    console.log ("Selected Index: " +index);
    this.updatediv = true;
    this.department = this.deptList[index];
    this.svc.update(this.department, this.indexposition);
  }

  delete(index:number)
  {
    this.svc.delete(index);
  }

}
