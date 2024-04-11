import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import 'rxjs/add/operator/catch';
import { API_URL } from '../env';
import { Command } from './command.model';
import { catchError } from 'rxjs/operators';
import { throwError } from 'rxjs';



@Injectable()
export class CommandsApiService{
    // ...

    private static _handleError(err: HttpErrorResponse | any) {
        return throwError(err.message || 'Error: Unable to complete request.');
    }

    // ...
}