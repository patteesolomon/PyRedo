export class Command {
    constructor(
        public name: string,
        public command: string,
        public _id?: number,
        public updatedAt?: Date,
        public createdAt?: Date,
        public lastUpdatedBy?: string,
    ) { }
}