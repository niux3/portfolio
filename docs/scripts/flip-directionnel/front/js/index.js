import '../scss/index.scss';

(()=>{
    let getDir = ($el, coordinates) =>{
        let w = $el.getBoundingClientRect().width,
			h = $el.getBoundingClientRect().height,

			/** calculate the x and y to get an angle to the center of the div from that x and y. **/
			/** gets the x value relative to the center of the DIV and "normalize" it **/
			x = ( coordinates.x - $el.offsetLeft - ( w/2 )) * ( w > h ? ( h/w ) : 1 ),
			y = ( coordinates.y - $el.offsetTop  - ( h/2 )) * ( h > w ? ( w/h ) : 1 ),

			/** the angle and the direction from where the mouse came in/went out clockwise (TRBL=0123);**/
			/** first calculate the angle of the point,
			add 180 deg to get rid of the negative values
			divide by 90 to get the quadrant
			add 3 and do a modulo by 4  to shift the quadrants to a proper clockwise TRBL (top/right/bottom/left) **/
			direction = Math.round( ( ( ( Math.atan2(y, x) * (180 / Math.PI) ) + 180 ) / 90 ) + 3 )  % 4;

		return direction;
    };

    let getClasses = direction =>{
        var fromClass, toClass, str_direction;
			switch( direction ) {
				case 0:
					// from top
                    str_direction = '-top';
					break;
				case 1:
					// from right
                    str_direction = '-right';
					break;
				case 2:
					// from bottom
                    str_direction = '-bottom';
					break;
				case 3:
					// from left
                    str_direction = '-left';
					break;
			};
            fromClass = `flip-from${str_direction}`;
            toClass = `flip${str_direction}`;
			return { from : fromClass, to: toClass };
    };
    let clearAnimate;
    document.querySelectorAll('.flip-card').forEach($el =>{

        ['mouseenter', 'mouseleave'].forEach(evenName =>{
            $el.addEventListener(evenName, e =>{
                let eventType = e.type,
                    direction = getDir( e.target, { x : event.pageX, y : event.pageY } ),
                    hoverClasses = getClasses( direction ),
                    $cardInner = $el.querySelector('.flip-card-inner'),
                    cls = null;
                switch (eventType){
                    case 'mouseenter':
                        console.log(hoverClasses.from);
                        $el.classList.add(hoverClasses.from);
                        cls = $el.className.match(/flip-from-(top|right|bottom|left)/);
                        if(cls !== null){
                            console.log('-->', cls);
                            $el.classList.remove(cls.shift());
                        }
                        clearTimeout(clearAnimate);
                        clearAnimate = setTimeout(()=>{
                            $el.classList.add('flip-animate');
                            $el.classList.add(hoverClasses.from);
                        },0);
                        break;
                    case 'mouseleave':
                        console.log(hoverClasses.to);
                        cls = $el.className.match(/flip-(top|right|bottom|left)/);
                        if(cls !== null){
                            console.log('-->', cls);
                            $el.classList.remove(cls.shift());
                        }
                        clearTimeout(clearAnimate);
                        clearAnimate = setTimeout(()=>{
                            $el.classList.add('flip-animate');
                            $el.classList.add(hoverClasses.to);
                        },0);

                        clearAnimate = setTimeout(()=>{
                            $el.classList.remove('flip-animate');
                            $el.classList.remove(hoverClasses.to);
                            cls = $el.className.match(/flip-from-(top|right|bottom|left)/);
                            if(cls !== null){
                                console.log('-->', cls);
                                $el.classList.remove(cls.shift());
                            }
                        },600);
                        break;
                }
            });
        })
    })
})()
