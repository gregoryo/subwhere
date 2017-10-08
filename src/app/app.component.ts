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
        console.log('data', data);
        this.userDataService.lat = data['location']['lat'];
        this.userDataService.lng = data['location']['lng'];
        console.log('lat', this.userDataService.lat); 
        console.log('lng', this.userDataService.lng); 
      })
    this.http.get('https://subwhere-182314.appspot.com/api/users')
      .subscribe(data => {
        console.log('data', data);
        this.userDataService.infos = data
      })
    };
}
