import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})


export class AppComponent {
  serverData
  val:string
  flag1:boolean=false;
  flag2:boolean=false;

  sendp()
  {
this.flag1=true;
this.flag2=false;
this.bz2();
  }

  sendp2(){
    this.flag2=true;
    this.flag1=false;
    this.gzip();
  }
  gzip(){
    this.val = "gzip"
  }

  bz2(){
    this.val = "bz2"
  }
  
  
  constructor(private httpClient: HttpClient) {
  }

  sendHi(fname) {
    var file_name = fname.split("\\")
    var file = file_name[file_name.length-1];
        

    this.httpClient.get('http://127.0.0.1:8000/'+file+"/"+this.val).subscribe(
      (response:any)=>this.serverData = response as JSON
    )
   
    
}}
