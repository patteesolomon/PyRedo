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
    http: any;
    // ...
    getCommands(): Observable<Command[]> {
        return this.http
            .get(`${API_URL}/commands`)
            .pipe(
                catchError(CommandsApiService._handleError)
            );
    }
    static _handleError(_handleError: any): any {
        throw new Error('Method not implemented.');
    }
}