import { Component, OnInit, OnDestroy } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Subscription } from 'rxjs';
import { CommandsApiService } from './commands/command-api.service';
import { Command } from './commands/command.model';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent implements OnInit, OnDestroy{
  title = 'webapp';
  commandListSubs: Subscription = new Subscription;
  commandList: Command[] = [];

  constructor(private commandsApi: CommandsApiService)
  { }
  ngOnInit(): void {
    this.commandListSubs = this.commandsApi
      .getCommands()
      .subscribe(res => {
        this.commandList = res;
        },
        console.error
      );
  }

  ngOnDestroy(): void {
    this.commandListSubs.unsubscribe();
  }
}

