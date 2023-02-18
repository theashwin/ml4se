@Bean
	@ConditionalOnMissingBean(PreDecorationFilter.class)
	public PreDecorationFilter preDecorationFilter(RouteLocator routeLocator,
			ProxyRequestHelper proxyRequestHelper) {
		return new PreDecorationFilter(routeLocator,
				this.server.getServlet().getContextPath(), this.zuulProperties,
				proxyRequestHelper);
	}