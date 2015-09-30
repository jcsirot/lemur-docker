package signbox;

import net.codestory.http.WebServer;
import net.codestory.http.payload.Payload;

/**
 * Created with IntelliJ IDEA.
 * User: jcsirot
 * Date: 30/09/15
 * Time: 11:16
 * To change this template use File | Settings | File Templates.
 */
public class Main
{
    public static void main(String[] args) {
        new WebServer().configure(
                routes -> routes.post("/certificate/enroll", (context) -> {
                    System.out.println(context.request().content());
                    return Payload.created();
                }))
                .start(9090);
    }
}
