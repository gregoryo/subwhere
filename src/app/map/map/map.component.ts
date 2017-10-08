import { Component, OnInit } from '@angular/core';
import {UserDataService} from '../../user-data.service';

@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent implements OnInit {

  constructor(private userDataService: UserDataService) { }
  lat;
  lng;
  ngOnInit() {
    console.log("I'm map");
    setTimeout(function(){
    this.lat = this.userDataService.lat;
    this.lng = this.userDataService.lng;
    console.log('I waited');
    }, 3000);
  }

}
