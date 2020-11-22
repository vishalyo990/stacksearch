import { Component, ViewChild } from '@angular/core';
import { StackserviceService } from './stackservice.service';
import { MatTableDataSource } from '@angular/material/table';
import {MatPaginator} from '@angular/material/paginator'
import { NgxSpinnerService } from 'ngx-spinner';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  @ViewChild(MatPaginator, { static: true }) paginator: MatPaginator;
  dataSource;
  displayedColumns: string[] = ['No questions available. Please use filters to search questions.'];

  constructor(private STACK_SERVICE:StackserviceService, public spinner: NgxSpinnerService){

  }

  async submit(values){

    this.spinner.show()
    let items = await this.STACK_SERVICE.fetch(values)
    this.prepare(items)
    this.spinner.hide()
  }

  prepare(items){
    this.displayedColumns =  ['Index', 'Questions'];
    let DATA = [];
    for (let i=0; i< items.length; i++){
      DATA.push({"Index":i, "Questions": items[i].link})
    }
    console.log(DATA)
    this.dataSource = new MatTableDataSource<any>(DATA);
    this.dataSource.paginator = this.paginator
    // console.log(this.dataSource)
  }

  openurl(elem) {
    window.open(elem.Questions, "_blank");
  }

}
