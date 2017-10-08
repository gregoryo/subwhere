import { Component } from '@angular/core';
import {UserDataService} from '../../user-data.service';

@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent{
  constructor(private userDataService: UserDataService) { }
  check(){
    for (let i=0; i<this.userDataService.infos;i++){
    console.log(this.userDataService.infos[i])
    }
  }
}
