public <T> T find(Connection conn, Collection<String> fields, Entity where, RsHandler<T> rsh) throws SQLException {
		final Query query = new Query(SqlUtil.buildConditions(where), where.getTableName());
		query.setFields(fields);
		return find(conn, query, rsh);
	}