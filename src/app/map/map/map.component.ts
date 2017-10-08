import { Component, OnInit } from '@angular/core';
import {UserDataService} from '../../user-data.service';

@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent implements OnInit {

  constructor(private userDataService: UserDataService) { }

  ngOnInit() {
    console.log("I'm map");
    console.log(this.userDataService.id);
    console.log(this.userDataService.position);
  }

}
