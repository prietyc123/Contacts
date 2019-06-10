import com.google.gdata.client.*;
import com.google.gdata.client.contacts.*;
import com.google.gdata.data.*;
import com.google.gdata.data.contacts.*;
import com.google.gdata.data.extensions.*;
import com.google.gdata.util.*;
import com.google.gdata.client.http.HttpGDataRequest;
import java.io.BufferedReader;
import java.io.ByteArrayOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.RandomAccessFile;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.List;
import java.util.logging.ConsoleHandler;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.awt.*;
import java.awt.event.*;


//Authorize Service object
ContactsService myService = new ContactsService("Unique Contact");

//Authorizing requests with OAuth 2.0
//Call URL for api connection

String URL = "https://accounts.google.com/o/oauth2/v2/auth?client_id=170460519931-gkr4n013brq70n140dlhthe55e5ruiqt.apps.googleusercontent.com&response_type=code&scope=https://www.googleapis.com&response_type=code&scope=https://www.googleapis.com/auth/gmail.send&redirect_uri=http://localhost&access_type=offline";

java.awt.Desktop.getDesktop().browser(java.net.URI.create(URL));

//Allow Permissions
String currentURL = null;
if( request.getAttribute("javax.servlet.forward.request_uri") != null ){
    currentURL = (String)request.getAttribute("javax.servlet.forward.request_uri");
}
if( currentURL != null && request.getAttribute("javax.servlet.include.query_string") != null ){
    currentURL += "?" + request.getQueryString();
}
var param1 = currentURL.extract();
var Code1 = (console.log(param1.code));
var ac;
var param2;
var accessToken;
public static void POSTRequest() throws IOException {   

    final String POST_PARAMS = "{\n" + 
        "    \"body\": \"code=Code1&client_id=170460519931-gkr4n013brq70n140dlhthe55e5ruiqt.apps.googleusercontent.com&client_secret=QiHbmS1WtGDwHwoXAdaQiYry&grant_type=authorization_code&redirect_uri=http://localhost\"" + "\n}";
    System.out.println(POST_PARAMS);
    URL obj = new URL("https://www.googleapis.com/oauth2/v4/token");
    HttpURLConnection postConnection = (HttpURLConnection) obj.openConnection();
    postConnection.setRequestMethod("POST");
    postConnection.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
    postConnection.setDoOutput(true);
    OutputStream os = postConnection.getOutputStream();
    ac = os.write(POST_PARAMS.getBytes());
    param2 = ac.extract();
    accessToken = (console.log(param2.access_token));
    int responseCode = postConnection.getResponseCode();
    System.out.println("POST Response Code :  " + responseCode);
    System.out.println("POST Response Message : " + postConnection.getResponseMessage());
}

//Google contacts

public class Contacts {
  
  private enum SystemGroup {
    MY_CONTACTS("Contacts", "My Contacts"),
    FRIENDS("Friends", "Friends"),
    FAMILY("Family", "Family"),
    COWORKERS("Coworkers", "Coworkers");

    private final String systemGroupId;
    private final String Name;

    SystemGroup(String systemGroupId, String Name) {
      this.systemGroupId = systemGroupId;
      this.Name = Name;
    }

    static SystemGroup fromSystemGroupId(String id) {
      for(SystemGroup group : SystemGroup.values()) {
        if (id.equals(group.systemGroupId)) {
          return group;
        }
      }
      throw new IllegalArgumentException("Unrecognized system group id: " + id);
    }

    @Override
    public String toString() {
      return Name;
    }
  }

  private final URL feedUrl;

  private final ContactsService service;
  
  private final String projection;

  private static String lastAddedId;

  private static final Logger httpRequestLogger =
      Logger.getLogger(HttpGDataRequest.class.getName());

  public Contacts(ContactsParameters parameters)
      throws MalformedURLException, AuthenticationException {
    projection = parameters.getProjection();
    String url = parameters.getBaseUrl()
        + (parameters.isGroupFeed() ? "groups/" : "contacts/")
        + parameters.getUserName() + "/" + projection;

    feedUrl = new URL(url);
    service = new ContactsService("Google-contactsApp");
    
    String userName = parameters.getUserName();
    String password = parameters.getPassword();
    if (userName == null || password == null) {
      return;
    }
    service.setUserCredentials(userName, password);
  }

  
  private void listEntries(ContactsParameters parameters)
      throws IOException, ServiceException {
    if (parameters.isGroupFeed()) {
      ContactGroupFeed groupFeed = 
          service.getFeed(feedUrl, ContactGroupFeed.class);    
      System.err.println(groupFeed.getTitle().getPlainText());
      for (ContactGroupEntry entry : groupFeed.getEntries()) {
        printGroup(entry);
      }
      System.err.println("Total: " + groupFeed.getEntries().size() + 
          " groups found");
    } else {
      ContactFeed resultFeed = service.getFeed(feedUrl, ContactFeed.class);
      // Print the results
      System.err.println(resultFeed.getTitle().getPlainText());
      for (ContactEntry entry : resultFeed.getEntries()) {
        printContact(entry);
      }
      System.err.println("Total: " + resultFeed.getEntries().size()
          + " entries found");
}

private static ContactEntry buildContact(
      ContactsParameters parameters) {
    ContactEntry contact = new ContactEntry();
    ElementHelper.buildContact(contact, parameters.getElementDesc());
    return contact;
}

//Main Class

public static void main(String[] args) throws ServiceException, IOException {

    POSTRequest();
    
    ContactsParameters parameters = new ContactsParameters(args);
    if (parameters.isVerbose()) {
      httpRequestLogger.setLevel(Level.FINEST);
      ConsoleHandler handler = new ConsoleHandler();
      handler.setLevel(Level.FINEST);
      httpRequestLogger.addHandler(handler);
      httpRequestLogger.setUseParentHandlers(false);
    }

    
    if (parameters.getUserName() == null || parameters.getPassword() == null) {
      System.err.println("Both username and password must be specified.");
      return;
    }
    
    if (parameters.isContactFeed() && parameters.isGroupFeed()) {
      throw new RuntimeException("Only one of contactfeed / groupfeed should" +
          "be specified");
    }

    Contacts sam = new Contacts(parameters);

    public void MyFile() 
    throws IOException {
    
    BufferedWriter writer = new BufferedWriter(new FileWriter(fileName));
    writer.write(sam);
     
    writer.close();
    }

    if (parameters.getScript() != null) {
      processScript(sam, parameters);
    } else {
      processAction(sam, parameters);
    }

   
    System.out.flush();
  }
}