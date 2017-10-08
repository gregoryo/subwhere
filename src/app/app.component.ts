import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { UserDataService } from './user-data.service'


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  title = 'SubWhere';
  subtitle = 'under the rainbow';
  lat = 0;
  lng = 0;

  constructor(private http: HttpClient, private userDataService: UserDataService) {}

  ngOnInit(){
    const body = {"considerIp": true};
    this.http.post('//www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyB-doYs2QnTeC3LM4feBjuwymtfh1A0-tQ', body)
      .subscribe(data => {
        this.lat = data['location']['lat'];
        this.lng = data['location']['lng'];
      })
    console.log(this.lat, this.lng);
    console.log(this.userDataService.id);
    this.userDataService.position = [this.lat, this.lng];
    console.log(this.userDataService.position); 
    };
}
