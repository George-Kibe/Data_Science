class SketchPad{
    constructor(container, size=400){
        this.canvas = document.createElement('canvas');
        this.canvas.width = size;
        this.canvas.height = size;
        this.canvas.style = `
            background-color: #fff;
            box-shadow: 0 0 10px 2px #000000;
        `
        container.appendChild(this.canvas);
        // detect mouse actions to draw
        this.ctx = this.canvas.getContext('2d');

        this.paths = [];
        this.isDrawing = false;

        this.#addEventListeners();
    }
    // internal function that can only be called inside this class
    #addEventListeners(){
        this.canvas.onmousedown = (event) => {
            const mouse = this.#getMouseLocation(event);
            this.paths.push([mouse]);
            this.isDrawing = true;
        }
        this.canvas.onmousemove = (event) => {
            if(this.isDrawing){
                const mouse = this.#getMouseLocation(event);
                const lastPath = this.paths[this.paths.length - 1];
                lastPath.push(mouse);
                // this.path.push(mouse);
                this.#redraw();
                console.log(this.paths.length)
            }            
        }
        this.canvas.onmouseup = () => {
            this.isDrawing = false;
        }        
    }

    #redraw(){
        this.ctx.clearRect(0, 0, 
            this.canvas.width, this.canvas.height);
        draw.paths(this.ctx, this.paths);
    }

    #getMouseLocation = (event) => {
        const rect = this.canvas.getBoundingClientRect();
        return [
            Math.round(event.clientX - rect.left), 
            Math.round(event.clientY - rect.top)
        ]
    }
}