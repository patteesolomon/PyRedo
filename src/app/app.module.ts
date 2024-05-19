import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { catchError } from 'rxjs/operators';
// import { Http } from '@angular/http';
import 'rxjs/add/operator/catch';
import { AppComponent } from './app.component';
import { CommandsApiService } from './commands/command-api.service';

@NgModule({
    declarations: [
        AppComponent
    ],
    imports: [
        BrowserModule,
        HttpClientModule,
    ],
    providers: [CommandsApiService],
    bootstrap: [AppComponent]
})
export class AppModule {
}