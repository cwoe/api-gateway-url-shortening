            <div id="formfield" class="is-3 is-offset-1 landing-caption">
                        <h3 class="subtitle is-5 is-spaced">
                        The URL requires a http:// or https:// in the beginning.
                        </h3>
                        <br/>
                        <br/>
                        <h3 class="subtitle is-4 is-spaced">
                                Your URL:
                        </h3>
                        <textarea id="longurl" name="message" cols="60" rows="3"></textarea>
                        <br/>
                        <br/>
                        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
                        <script>
                                $(document).ready(function(){
                                        $("button").click(function(){
                                                $.get("https://qh0vvagpvi.execute-api.eu-west-1.amazonaws.com/prod/shorten/?longurl=" +>
                                                        function(data, status){
                                                                document.getElementById("formfield").innerHTML = data.shorturl;
                                        });
                                });
                        });
                        </script>
                        <button>Shorten URL</button>
                    </div>
