<script>
    let isAppointment = false,
        onCaptcha = e => e.target.value = e.target.value.toUpperCase(),
        onSubmit = e =>{
            console.log(e)
        }
</script>
<div class="contact">
    <div class="wrap-contact">
        <h1>Travaillons ensemble</h1>
        <p class="intro">proposition de carrière &#x2022; me dire bonjour</p>
        <form method="post" on:submit|preventDefault={onSubmit}>
            <div class="col">
                <div class="input text cell-6">
                    <label>
                        <span>Prénom</span>
                        <input type="text" name="firstname">
                    </label>
                </div>
                <div class="input text required cell-6">
                    <label>
                        <span>Nom</span>
                        <input type="text" name="lastname">
                    </label>
                </div>
            </div>
            <div class="col">
                <div class="input text required cell-6">
                    <label>
                        <span>Email</span>
                        <input type="text" name="email">
                    </label>
                </div>
                <div class="input text required cell-6">
                    <label>
                        <span>Sujet</span>
                        <input type="text" name="subject">
                    </label>
                </div>
            </div>
            <div class="col">
                <div class="cell-4 input checkbox">
                    <label>
                        <input type="checkbox" name="appointment" bind:checked={isAppointment}>
                        <span>Prendre rendez vous avec moi&nbsp;?&nbsp;</span>
                    </label>
                </div>
                <div class="cell-4 input date {isAppointment? 'required' : ''}">
                    <label style={isAppointment? 'height:100%' : 'height:0%'}>
                        <span>Date</span>
                        <input type="date" name="date_appointment" class="{isAppointment? 'required' : ''}">
                    </label>
                </div>
                <div class="cell-4 input time {isAppointment? 'required' : ''}">
                    <label style={isAppointment? 'height:100%' : 'height:0%'}>
                        <span>Heure</span>
                        <input type="time" min="09:00" max="18:00" name="hour_appointment" class="{isAppointment? 'required' : ''}">
                    </label>
                </div>
            </div>
            <input type="text" name="address" value="">
            <div class="input textarea required">
                <label>
                    <span>Message</span>
                    <textarea name="message"></textarea>
                </label>
            </div>
            <div class="col">
                <div class="cell-4">
                    <div class="col captcha-pattern">
<pre class="cell-3">
     █████╗ 
    ██╔══██╗
    ███████║
    ██╔══██║
    ██║  ██║
    ╚═╝  ╚═╝
</pre>
<pre class="cell-3">
     ███████╗
     ██╔════╝
     █████╗  
     ██╔══╝  
     ██║     
     ╚═╝     
</pre>
<pre class="cell-3">
     ███╗   ███╗
     ████╗ ████║
     ██╔████╔██║
     ██║╚██╔╝██║
     ██║ ╚═╝ ██║
     ╚═╝     ╚═╝
</pre>
<pre class="cell-3">
     ██╗    ██╗
     ██║    ██║
     ██║ █╗ ██║
     ██║███╗██║
     ╚███╔███╔╝
      ╚══╝╚══╝ 
</pre>
                    </div>
                </div>
                <div class="cell-4">
                    <div class="input text required no-margin">
                        <label>
                            <span>Recopier le motif</span>
                            <input type="text" maxlength="4" name="captcha" on:input={onCaptcha}>
                        </label>
                    </div>
                </div>
                <div class="cell-4">
                    <div class="input submit">
                        <button type="submit">envoyer</button>
                    </div>
                </div>
            </div>
        </form>
    </div>
</div>
<style lang="scss">
    .contact{
        display: flex;
        flex-direction:column;
        height: 100%;

        input[name="address"]{
            position: absolute;
            top: -500000px;
        }

        .wrap-contact{
            margin: auto;
            width: 100%;
            
            h1, .intro{
                text-transform: uppercase;
                text-align: center;
            }

            h1{
                margin-bottom: 0;
            }
            
            form{
                label{
                    display: block;
                    text-transform: uppercase;
                    font-size: .8rem;
                }
                .captcha-pattern{
                    height: 100%;
                    pre{
                        font-size: .5vw;
                        overflow: hidden;
                        margin: auto 0;
                    }
                }
                
                .input{
                    &.text, 
                    &.date,
                    &.time,
                    &.textarea{
                        margin-bottom: 25px;

                        &.no-margin{
                            margin: 0;
                        }

                        label > span:first-of-type{
                            display: inline-block;
                            margin-bottom: 10px;
                        }
                        input, textarea{
                            width: 100%;
                            height: 50px;
                            border-radius: 3px;
                            border: 1px solid darken(#f5f5f5, 30%);
                            font-size: 1rem;
                            padding: 0 15px;
                            background-color: darken(#f5f5f5, 5%);
                            transition: border-color 400ms, background-color 400ms;

                            &:focus, &:active{
                                outline:none !important;
                                border-color: darken(#f5f5f5, 70%);
                                background-color: #f5f5f5;
                            }
                        }

                        textarea{
                            padding: 15px;
                            height: 100%;
                        }
                    }

                    &.checkbox{
                        margin: auto 0;
                    }

                    &.required{
                        label > span:first-of-type{
                            &:after{
                                content : ' *';
                                color: red;
                                font-weight: 600;
                            }
                        }
                    }

                    &.date, 
                    &.time {
                        label{
                            height: 0%;
                            transition: height 400ms;
                            overflow: hidden;

                            &.animate{
                                height: 100%;
                            }
                        }
                    }

                    &.submit{
                        height: 100%;
                        display: flex;
                        align-items: end;

                        button{
                            border: 1px solid #444;
                            text-transform: uppercase;
                            width: 100%;
                            height: 50px;
                            border-radius:3px;
                            margin-bottom: 8px;
                        }
                    }
                }
            }
        }

        .col{
            display: flex;
            justify-content:space-between;

            .cell-6{
                width: 49%;
            }

            .cell-3{
                width: 24%;
            }

            .cell-4{
                width: 32%;
            }
        }
    }
</style>

