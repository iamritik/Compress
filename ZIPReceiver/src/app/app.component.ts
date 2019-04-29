import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})


export class AppComponent {
  serverData
  
  
  
  constructor(private httpClient: HttpClient) {
  }

  sendHi() {
    
    this.httpClient.get('http://127.0.0.1:8001/').subscribe(
      (response:any)=>this.serverData = response as JSON
    )
    

    
}}
