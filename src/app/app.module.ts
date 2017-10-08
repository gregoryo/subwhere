import { BrowserModule } from '@angular/platform-browser';
import { Component, NgModule} from '@angular/core';

import { AppComponent } from './app.component';
import { MapComponent } from './map/map/map.component';
import { InputComponent } from './map/input/input.component';
import { HttpClientModule } from '@angular/common/http';

import { AgmCoreModule } from '@agm/core';
import { UserDataService } from './user-data.service';


@NgModule({
  declarations: [
    AppComponent,
    MapComponent,
    InputComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AgmCoreModule.forRoot({
      apiKey: 'AIzaSyB-doYs2QnTeC3LM4feBjuwymtfh1A0-tQ'
    })
  ],
  providers: [UserDataService],
  bootstrap: [AppComponent]
})
export class AppModule {
}
