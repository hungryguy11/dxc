import { Injectable } from '@angular/core';
import { Department } from './department';

@Injectable({
  providedIn: 'root'
})
export class DepartmentService {

  deptList : Department[] =[];

  constructor() { }

  save(dep: Department)
  {

    this.deptList.push(dep);

  }

  update(dep : Department, index : number)
  {

    this.deptList[index] = dep;

  }

  delete(index:number)
  {
    this.deptList.splice(index,1);
  }
}
