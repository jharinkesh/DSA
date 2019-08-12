package com.demo.progs;

import java.util.Hashtable;

import javax.naming.AuthenticationException;
import javax.naming.AuthenticationNotSupportedException;
import javax.naming.Context;
import javax.naming.NamingEnumeration;
import javax.naming.NamingException;
import javax.naming.directory.Attributes;
import javax.naming.directory.DirContext;
import javax.naming.directory.InitialDirContext;
import javax.naming.directory.SearchControls;
import javax.naming.directory.SearchResult;

public class LDAPTest {

	static DirContext context;

	public static void main(String[] args) throws Exception {
		setConnection();
//		final SearchControls searchControls = new SearchControls();
//		searchControls.setSearchScope(SearchControls.SUBTREE_SCOPE);
//		NamingEnumeration<?> namingEnum = context.search("dc=jboss,dc=org", "(uid=*)", searchControls);
//		while (namingEnum.hasMore()) {
//			SearchResult sr = (SearchResult) namingEnum.next();
//			Attributes attrs = sr.getAttributes();
//			System.out.println(attrs.get("cn"));
//		}
//		namingEnum.close();
		//search("DC=dominio_general,OU=org", "userType=Admin", {"username", "mail"});
		String searchFilters = "(objectClass=inetOrgPerson)";
		String[] requiredAtrributes = {"cn","sn","uid"};
		SearchControls controls = new SearchControls();
		controls.setSearchScope(SearchControls.SUBTREE_SCOPE);
		controls.setReturningAttributes(requiredAtrributes);
		NamingEnumeration users = context.search("uid=jduke,ou=Users,dc=jboss,dc=org", searchFilters, controls);
		while(users.hasMore()){
			SearchResult result = (SearchResult)users.next();
			Attributes attributes = result.getAttributes();
			System.out.println(attributes.get("cn").get(0).toString());
		}
		
	}

//	public static void search (String search, String filter, String[] returningAtts) throws NamingException{ 
//	    SearchControls ctls = new SearchControls();
//	    ctls. setReturningObjFlag (true); 
//	    
//	    ctls.setReturningAttributes(returningAtts);
//	    ctls.setSearchScope(SearchControls.OBJECT_SCOPE);
//
//	    NamingEnumeration answer = context.search(search,filter, ctls);  
//	    while (answer.hasNext()){
//	        SearchResult result = (SearchResult) answer.next();
//	        HashMap map = new HashMap();
//	        for (String returning : returningAtts){
//	             map.put(returning, result.getAttributes().get("returning").get().toString());
//	        }
//	        doSomething(map);
//	    }     	
//	}	
	
	static void setConnection() {
		Hashtable<String, String> environment = new Hashtable<String, String>();
		environment.put(Context.INITIAL_CONTEXT_FACTORY, "com.sun.jndi.ldap.LdapCtxFactory");
		environment.put(Context.PROVIDER_URL, "ldap://127.0.0.1:10389");
		environment.put(Context.SECURITY_AUTHENTICATION, "simple");
		environment.put(Context.SECURITY_PRINCIPAL, "uid=admin,ou=system");
		environment.put(Context.SECURITY_CREDENTIALS, "secret");
		try {
			context = new InitialDirContext(environment);
			System.out.println("Connected..");
			System.out.println(context.getEnvironment());
			//context.close();
		} catch (AuthenticationNotSupportedException exception) {
			System.out.println("The authentication is not supported by the server");
		} catch (AuthenticationException exception) {
			System.out.println("Incorrect password or username");
		} catch (NamingException exception) {
			System.out.println("Error when trying to create the context");
		}
	}


//https://www.hexacta.com/2015/03/18/java-for-dummies-ldap-server/
//https://www.javacodegeeks.com/2015/09/java-to-ldap-tutorial-including-how-to-install-an-ldap-server-client.html
//http://www.java2s.com/Code/Java/JNDI-LDAP/LDAPSearch.htm
}
