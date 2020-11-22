import { Injectable } from '@angular/core';
import { HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class StackserviceService {

  constructor(private httpClient: HttpClient) { }

  async fetch(value){
      let payload = value
      console.log(value)
    let response: any = await this.httpClient.post("http://127.0.0.1:8000/",payload).toPromise()
    return response.items
  }
}


