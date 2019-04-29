import { Injectable } from '@angular/core';
import {Http ,Response} from '@angular/http';
import 'rxjs'
@Injectable({
  providedIn: 'root'
})
export class RestService {

  readUrl: string="http://127.0.0.1:50000/readFile/"
  constructor(private http:Http) { }
asd
readFile(file_name)
  {
    console.log(file_name);
    //console.log(format);
    //console.log(file_text);
    let arr = [file_name] 
    return this.http.get(this.readUrl+arr)
    //.subscribe((response : any ) => response.json()); 
    .subscribe((response : any ) => this.asd=response); 
  }


}
